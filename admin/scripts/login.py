from selenium.webdriver.common.by import By

from admin.tools.edgeDriver import *

# 页面操作
driver = get_EdgeDriver("http://192.168.249.130/index.php/index.php/Admin/Admin/login")

# 输入用户名
driver.find_element(By.NAME, "username").send_keys("admin")

# 输入密码
driver.find_element(By.NAME, "password").send_keys("123456")

# 输入验证码
driver.find_element(By.ID, "vertify").send_keys("8888")

# 点击登录
driver.find_element(By.CLASS_NAME, "sub").click()

quit_driver(driver)
