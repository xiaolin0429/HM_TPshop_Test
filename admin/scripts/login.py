from selenium.webdriver.common.by import By

from admin.tools.edgeDriver import *

# 页面操作
driver = get_EdgeDriver("https://hmshop-test.itheima.net/index.php/Admin/Admin/login")

# 输入用户名
driver.find_element(By.NAME, "username").send_keys("admin")

# 输入密码
driver.find_element(By.NAME, "password").send_keys("HM_2023_test")

# 输入验证码
driver.find_element(By.ID, "vertify").send_keys("8888")

# 点击登录
driver.find_element(By.CLASS_NAME, "sub").click()

quit_driver(driver)
