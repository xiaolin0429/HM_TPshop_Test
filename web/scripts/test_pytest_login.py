import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 这里添加测试数据按照(username, password, verify_code, expected_result)格式填入
login_test_data = [
    ("", "123456", "8888", "用户名不能为空!"),
    ("13788884444", "123456", "8888", "账号不存在!"),
    ("13812347863", "", "8888", "密码不能为空!"),
    ("13812347863", "55555", "8888", "密码错误!"),
    ("13812347863", "123456", "", "验证码不能为空!"),
    ("13812347863", "123456", "4444", "验证码错误"),
    ("13812347863", "123456", "8888", "13812347863")
]


class TestLogin:
    # 类前置处理
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Edge()
        self.driver.maximize_window()  # 最大化浏览器窗口
        self.driver.implicitly_wait(5)  # 隐式等待

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

    @pytest.mark.parametrize("username, password, verify_code, expected_result", login_test_data)
    def test_login(self, username, password, verify_code, expected_result):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys(username)

        # 密码
        self.driver.find_element(By.ID, "password").send_keys(password)

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys(verify_code)

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()

        time.sleep(2)
        # 判断预期结果是否为用户名，如果是，说明登录成功，否则登录失败
        if expected_result == username:
            # 断言实际的用户名是否与预期的用户名相符
            assert expected_result == self.driver.find_element(By.CLASS_NAME, "userinfo").text
        else:
            # 显式等待
            wait = WebDriverWait(self.driver, 10)
            # 获取实际的错误消息
            actual_error = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]"))).text
            # 打印实际的错误消息
            print(actual_error)
            # 断言实际的错误消息是否与预期的错误消息相符
            assert expected_result == actual_error
