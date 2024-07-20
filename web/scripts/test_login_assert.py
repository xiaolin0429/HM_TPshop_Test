import time

from selenium import webdriver
from selenium.webdriver.common.by import By


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

    def test_login01(self):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()
        time.sleep(2)
        # 断言
        print(
            self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text)
        assert "用户名不能为空!" in self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text

    def test_login02(self):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("13812347863")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()
        time.sleep(2)
        # 断言
        print(
            self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text)
        assert "密码不能为空!" in self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text

    def test_login03(self):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("13812347863")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()
        time.sleep(2)
        # 断言
        print(
            self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text)
        assert "验证码不能为空!" in self.driver.find_element(By.XPATH, "//*[@class='layui-layer layui-layer-dialog  layer-anim']/div[2]").text

    def test_login04(self):
        # 用户名
        self.driver.find_element(By.ID, "username").send_keys("13812347863")

        # 密码
        self.driver.find_element(By.ID, "password").send_keys("123456")

        # 验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录
        self.driver.find_element(By.NAME, "sbtbutton").click()
        time.sleep(2)
        # 断言
        print(self.driver.find_element(By.CLASS_NAME, "userinfo").text)
        assert "13812347863" == self.driver.find_element(By.CLASS_NAME, "userinfo").text
