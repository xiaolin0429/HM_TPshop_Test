import json
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def load_test_data():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, '..', 'test_data_json', 'address_test_data.json')
    with open(json_path, 'r', encoding='UTF-8') as file:
        return json.load(file)


class TestAddressAdd:
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()
        print("收货地址添加测试结束")

    def setup_method(self):
        self.driver.get("http://172.22.175.97/index.php/Home/Index/index.html")

    def teardown_method(self):
        self.driver.back()

    def login(self):
        # 登录
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("13812347863")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()

    @pytest.mark.parametrize("consignee, mobile, address, zipcode", load_test_data())
    def test_address_add(self, consignee, mobile, address, zipcode):
        """
        收货地址添加测试
        :param consignee: 收货人
        :param mobile: 手机号
        :param address: 详细地址
        :param zipcode: 邮编
        :return:
        """
        # 判断是否已登录
        try:
            login_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "登录")))
            print("未登录，执行登录操作")
            self.login()
            time.sleep(2)
        except:
            print("已登录，跳过登录操作")
        self.driver.find_element(By.XPATH, "//*[@class='fl islogin hide']/a[1]").click()
        print("开始执行收货地址添加测试")
        self.driver.find_element(By.LINK_TEXT, "地址管理").click()
        self.driver.find_element(By.XPATH, "//*[@class='address']/span").click()

        # 收货人
        self.driver.find_element(By.XPATH, "//*[@class='ui-switchable-panel']/div[1]/div/input") \
            .send_keys(consignee)

        # 收货人手机
        self.driver.find_element(By.XPATH, "//*[@class='ui-switchable-panel']/div[2]/div/input") \
            .send_keys(mobile)

        # 收货地址
        select = Select(self.driver.find_element(By.ID, "province"))  # 省
        select.select_by_value("33007")
        time.sleep(1)
        select = Select(self.driver.find_element(By.ID, "city"))  # 市
        select.select_by_value("33008")
        time.sleep(1)
        select = Select(self.driver.find_element(By.ID, "district"))  # 区
        select.select_by_value("33163")

        # 详细地址
        self.driver.find_element(By.XPATH, "//*[@class='ui-switchable-panel']/div[4]/div/input") \
            .send_keys(address)

        # 邮编
        self.driver.find_element(By.XPATH, "//*[@class='ui-switchable-panel']/div[5]/div/input") \
            .send_keys(zipcode)
        # 保存
        self.driver.find_element(By.XPATH, "//*[@class='ui-switchable-panel']/div[6]/div/div/button") \
            .click()
