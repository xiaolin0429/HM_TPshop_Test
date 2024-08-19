import json
import os
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


# 加载测试数据
def load_test_data():
    """
    加载登录测试所需的用户名、密码、验证码和预期结果数据。

    Returns:
        list: 包含测试数据的列表，每个元素都是一个包含用户名、密码、验证码和预期结果的元组。
    """
    base_dir = os.path.dirname(__file__)  # 获取当前文件所在的目录
    json_path = os.path.abspath(os.path.join(base_dir, '..', 'test_data_json', 'login_test_data.json'))
    with open(json_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return [(item["username"], item["password"], item["vertify"], item["expected_result"]) for item in data]


# 登录测试类
class TestLogin:
    # 类前置处理
    def setup_class(self):
        """
        在整个测试类开始之前进行初始化设置。
        """
        # 打开浏览器
        self.driver = webdriver.Edge()
        self.driver.maximize_window()  # 最大化浏览器窗口
        self.driver.implicitly_wait(5)  # 隐式等待

    # 类后置处理
    def teardown_class(self):
        """
        在整个测试类结束后进行清理。
        """
        self.driver.quit()

    # 方法前置处理
    def setup_method(self):
        """
        在每个测试方法开始之前进行初始化设置。
        """
        # 打开浏览器页面
        self.driver.get("http://192.168.140.129/index.php/Admin/Admin/login")

    # 方法后置处理
    def teardown_method(self):
        """
        在每个测试方法结束后进行清理。
        """
        time.sleep(3)

    # 测试登录功能
    @pytest.mark.parametrize("username, password, vertify, expected_result", load_test_data())
    def test_login(self, username, password, vertify, expected_result):
        """
        测试登录功能是否按照预期工作。

        Parameters:
            username (str): 测试用的用户名。
            password (str): 测试用的密码。
            vertify (str): 测试用的验证码。
            expected_result (str): 预期的测试结果。
        """
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "vertify").send_keys(vertify)
        # time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "sub").click()

        # 尝试查找是否存在登录错误的提示。
        try:
            error_msg = self.driver.find_element(By.XPATH, "//*[@id='error']/span").text
            assert error_msg == expected_result
        except NoSuchElementException:
            # 如果找不到错误提示，则说明登录成功，可以断言页面标题是否为“TPshop开源商城”
            assert self.driver.title == "TPshop开源商城"
