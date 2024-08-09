from selenium.webdriver.common.by import By

from web.tools.edgeDriver import get_EdgeDriver, quit_driver

# 打开浏览器页面
driver = get_EdgeDriver("http://192.168.140.129/index.php")

# 进入登录页面
driver.find_element(By.LINK_TEXT, "登录").click()

# 用户名
driver.find_element(By.ID, "username").send_keys("13812347863")

# 密码
driver.find_element(By.ID, "password").send_keys("123456")

# 验证码
driver.find_element(By.ID, "verify_code").send_keys("8888")

# 点击登录
driver.find_element(By.NAME, "sbtbutton").click()

quit_driver(driver)
