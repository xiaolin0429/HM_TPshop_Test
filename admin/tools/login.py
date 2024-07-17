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
    driver = get_EdgeDriver("http://192.168.249.130/index.php/Admin/Admin/login")
    # 登录
    login(driver, "admin", "123456", "8888")
    # 返回
    return driver
