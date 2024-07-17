import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

login_test_data = [
    ("", "123456", "8888"),
    ("13812347863", "", "8888"),
    ("13812347863", "123456", ""),
    ("13812347863", "123456", "8888")
]


class TestLogin:
    # 类前置处理
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Edge()
        self.driver.maximize_window()  # 最大化浏览器窗口
        self.driver.implicitly_wait(10)  # 隐式等待

    # 类后置处理
    def teardown_class(self):
        self.driver.quit()

    # 方法前置处理
    def setup_method(self):
        # 打开浏览器页面
        self.driver.get("http://192.168.249.129/index.php/Home/user/login.html")

    # 方法后置处理
    def teardown_method(self):
        time.sleep(3)

    @pytest.mark.parametrize("username, password, verify_code", login_test_data)
    def test_login(self, username, password, verify_code):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys(username)

        # 密码
        self.driver.find_element(By.ID, "password").send_keys(password)

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys(verify_code)

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()

        print(self.driver.find_element(By.CLASS_NAME, "userinfo").text)
        assert "13812347863" == self.driver.find_element(By.CLASS_NAME, "userinfo").text
