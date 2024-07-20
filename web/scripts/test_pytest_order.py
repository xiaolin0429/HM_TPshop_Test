import time

from selenium import webdriver

# 测试用例数据
register_test_data = [

]


class TestRegister:

    #类前置处理
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  #隐式等待

    # 类后置处理
    def teardown_class(self):
        self.driver.quit()

    # 方法前置处理
    def setup_method(self):
        # 打开页面首页
        self.driver.get("http://192.168.249.129/index.php")

    # 方法后置处理
    def teardown_method(self):
        self.driver.refresh()
        time.sleep(2)

    # 下面是添加订单的操作步骤

