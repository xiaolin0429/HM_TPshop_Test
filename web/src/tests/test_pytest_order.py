import json
import os
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 调用测试数据
def load_test_data():
    base_dir = os.path.dirname(__file__)  # 获取当前文件所在的目录
    json_path = os.path.join(base_dir, '..', 'test_data_json', 'order_test_data.json')
    with open(json_path, 'r', encoding='UTF-8') as file:
        return json.load(file)


class TestOrder:

    # 类前置处理
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 隐式等待

    # 类后置处理
    def teardown_class(self):
        self.driver.quit()

    # 方法前置处理
    # 显示等待
    @pytest.fixture(autouse=True)
    def setup_method(self):
        # 打开页面首页
        self.driver.get("http://172.22.175.97/index.php")
        # 进入登录页面
        self.driver.find_element(By.LINK_TEXT, "登录").click()

        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("13812347863")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()

    # 方法后置处理
    def teardown_method(self):
        self.driver.refresh()
        # 因为在测试方法进行前先进行了登录，然后用例需要连续进行操作，所以需要将前面登录的账号退出
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "退出").click()
        time.sleep(2)

    # 下面是添加订单的操作步骤
    @pytest.mark.parametrize("goods, expected_result", load_test_data())
    def test_order(self, goods, expected_result):
        # 进入首页
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "首页").click()
        # 使用搜索框输入商品名称
        self.driver.find_element(By.ID, "q").send_keys(goods)

        # 点击搜索按钮
        self.driver.find_element(By.CLASS_NAME, "ecsc-search-button").click()

        # 等待搜索结果页面加载
        wait = WebDriverWait(self.driver, 10)
        product_element = None  # 在 try 块外部定义变量
        try:
            # 检查是否存在商品元素
            product_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-btn")))
            product_exists = True
        except TimeoutException:
            print("未找到商品元素")
            product_exists = False

        # 如果有商品，继续执行以下步骤
        if product_exists:
            # 将指定商品加入购物车
            product_element.click()

            # 处理商品库存不足的弹窗
            try:
                stock_alert = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//*[@class='layui-layer-content layui-layer-padding']")))
                stock_alert_text = stock_alert.text.strip()
                print(f"Found stock alert popup with content: {stock_alert_text}")  # 打印弹窗内容

                # 断言弹窗内容
                if expected_result == "商品库存不足，剩余0,当前购物车已有0件":
                    assert stock_alert_text == expected_result, f"Expected '{expected_result}', but got '{stock_alert_text}'"

                    # 点击 '确定' 按钮关闭弹窗
                    close_button = self.driver.find_element(By.XPATH, "//*[@class='layui-layer-btn0']")
                    close_button.click()

                    return  # 结束测试用例
            except TimeoutException:
                print("未找到库存不足弹窗")
                if expected_result == "商品库存不足，剩余0,当前购物车已有0件":
                    assert False, "未找到库存不足弹窗"
                # 继续执行后面的逻辑

            # 点击去购物车结算
            try:
                fram = self.driver.find_element(By.ID, "layui-layer-iframe1")
                self.driver.switch_to.frame(fram)
                time.sleep(1)
                self.driver.find_element(By.LINK_TEXT, "去购物车结算").click()
                self.driver.switch_to.default_content()
            except NoSuchElementException:
                print("未找到去购物车结算按钮或iframe")

            # 进入购物车界面后点击去结算
            self.driver.find_element(By.CLASS_NAME, "paytotal").click()

            # 处理alert弹窗
            try:
                time.sleep(1)
                self.driver.switch_to.alert.accept()
            except NoAlertPresentException:
                print("未找到alert弹窗")

            # 提交订单
            self.driver.find_element(By.ID, "submit_order").click()

            # 确认支付方式
            self.driver.find_element(By.LINK_TEXT, "确认支付方式").click()

            # 等待订单提交成功页面加载
            try:
                success_message_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "erhuh")))
                success_message = success_message_element.text
                assert expected_result in success_message, f"Expected '{expected_result}' to be in '{success_message}'"
            except TimeoutException:
                print("订单提交成功页面加载失败")
                if expected_result == "订单提交成功，我们将在第一时间给你发货！":
                    assert False, "订单提交成功页面加载失败"
        else:
            # 如果没有商品，断言失败
            text = self.driver.find_element(By.CLASS_NAME, "ncyekjl").text
            assert text == expected_result
