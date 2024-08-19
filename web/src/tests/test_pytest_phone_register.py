import json
import os
import time

import pymysql
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 调用测试数据
def load_test_data():
    base_dir = os.path.dirname(__file__)  # 获取当前文件所在的目录
    json_path = os.path.join(base_dir, '..', 'data', 'register_test_data.json')
    with open(json_path, 'r', encoding='UTF-8') as file:
        return json.load(file)


class TestRegister:

    # 类前置处理
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 隐式等待

    # 类后置处理
    def teardown_class(self):
        self.driver.quit()

    # 方法前置处理
    def setup_method(self):
        # 打开注册页面
        self.driver.get("http://192.168.140.129/index.php/Home/user/reg.html")

    # 方法后置处理
    def teardown_method(self):
        self.driver.refresh()
        time.sleep(2)

    # 测试用例方法
    @pytest.mark.parametrize("username, verify_code, password, password2, invite, expected_result", load_test_data())
    def test_register(self, username, verify_code, password, password2, invite, expected_result):
        # 输入用户名(手机号）
        self.driver.find_element(By.ID, "username").send_keys(username)

        # 图像验证码
        self.driver.find_element(By.NAME, "verify_code").send_keys(verify_code)

        # 输入密码
        self.driver.find_element(By.ID, "password").send_keys(password)

        # 输入确认密码
        self.driver.find_element(By.ID, "password2").send_keys(password2)

        # 推荐人手机
        self.driver.find_element(By.NAME, "invite").send_keys(invite)

        # 点击同意协议并注册
        if not self.driver.find_element(By.ID, "checktxt").is_selected():
            self.driver.find_element(By.ID, "checktxt").click()
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "同意协议并注册")

        # 使用driver自带的js库直接操作点击注册按钮
        self.driver.execute_script("arguments[0].click();", element)

        time.sleep(1)

        # 判断预期结果是否为用户名，如果是，说明登录成功，否则登录失败
        if expected_result == username:

            # 断言实际的用户名是否与预期的用户名相符
            assert expected_result == self.driver.find_element(By.CLASS_NAME, "userinfo").text

            # 从mysql数据库删除注册成功的账号，便于后期重复运行此注册测试脚本
            conn = pymysql.connect(host="192.168.140.129", user="root", password="123456", db="tpshop3.0", port=3306)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tp_users WHERE mobile = %s", username)
            conn.commit()
            cursor.close()
            conn.close()

        else:
            # 显式等待
            wait = WebDriverWait(self.driver, 10)
            try:
                # 尝试获取弹窗
                time.sleep(1)
                print("*" * 80)
                popup = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@class='layui-layer layui-anim layui-layer-dialog ']/div[2]")))
                # 如果弹窗存在，根据弹窗的文本内容来决定是否需要关闭它
                if popup:
                    popup_text = popup.text
                    if "密码有效长度为6-16位！" in popup_text:  # 根据实际的错误消息来调整
                        self.driver.find_element(By.XPATH,
                                                 "//*[@class='layui-layer layui-anim layui-layer-dialog ']/div[2]/a").click()
            except Exception as e:
                print(f"没有找到弹窗: {e}")

            # 获取实际的错误消息
            actual_error = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@class='layui-layer layui-anim layui-layer-dialog ']/div[2]"))).text
            # 打印实际的错误消息
            print(actual_error)
            # 断言实际的错误消息是否与预期的错误消息相符
            assert expected_result in actual_error
