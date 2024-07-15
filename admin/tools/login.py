"""
    登录
"""

from selenium.webdriver.common.by import By
from admin.tools.edgeDriver import get_EdgeDriver


def login(driver, username, password, vertify):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "vertify").send_keys(vertify)
    driver.find_element(By.CLASS_NAME, "sub").click()


def get_login():
    # 页面操作
    driver = get_EdgeDriver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")
    # 登录
    login(driver, "admin", "HM_2023_test", "8888")
    # 返回
    return driver
