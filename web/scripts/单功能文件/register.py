import time
from random import randint

from selenium.webdriver.common.by import By

from web.tools.edgeDriver import get_EdgeDriver, quit_driver

# 打开网页
driver = get_EdgeDriver("http://192.168.249.129/index.php")

# 页面操作
# 进入注册页面
time.sleep(1)
driver.find_element(By.LINK_TEXT, "注册").click()

#进入手机注册流程
time.sleep(1)
driver.find_element(By.LINK_TEXT, "手机注册").click()

# 输入手机号码(后四位数字随机）
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys(f"138{randint(10000000, 99999999)}")
# driver.find_element(By.NAME, "username").send_keys("13812347863")

# 输入图像验证码
driver.find_element(By.NAME, "verify_code").send_keys("8888")

# 设置密码
driver.find_element(By.ID, "password").send_keys("123456")

# 确认密码
driver.find_element(By.ID, "password2").send_keys("123456")

# 推荐人手机
driver.find_element(By.NAME, "invite").send_keys("")

# 判断是否以默认点击同意协议
if not driver.find_element(By.ID, "checktxt").is_selected():
    driver.find_element(By.ID, "checktxt").click()

# 点击注册按钮
driver.find_element(By.CSS_SELECTOR, "#reg_form2 > div > div > div > div.line.liney.clearfix > div > a").click()

# 退出浏览器
time.sleep(3)
quit_driver(driver)
