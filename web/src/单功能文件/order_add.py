import time

from selenium.webdriver.common.by import By

from web.tools.edgeDriver import quit_driver
from web.tools.login import login

# 打开浏览器页面
driver = login()
driver.implicitly_wait(5)
# time.sleep(1)
# 返回首页
driver.find_element(By.LINK_TEXT, "首页").click()

# 使用搜索框搜索商品名称
driver.find_element(By.ID, "q").send_keys("iPhone 14 Pro Max")
# 点击搜索
driver.find_element(By.CLASS_NAME, "ecsc-search-button").click()

# 将指定商品加入购物车
# time.sleep(1)
driver.find_elements(By.CLASS_NAME, "p-btn")[1].click()

# # 点击去购物车结算
# time.sleep(1)
# driver.switch_to.frame(By.ID, "layui-layer-iframe1")
# time.sleep(1)
# driver.find_element(By.LINK_TEXT, "去购物车结算").click()
# driver.switch_to.default_content()

# 关闭提示窗口
# time.sleep(1)
driver.find_element(By.CLASS_NAME, "layui-layer-setwin").click()

# 点击购物车
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".c-n.fl").click()

# 进入购物车界面后点击去结算
# time.sleep(1)
driver.find_element(By.CLASS_NAME, "paytotal").click()

# # 弹出登录窗口后，进行登录操作
# time.sleep(1)
# driver.find_element(By.ID, "username").send_keys("13812347863")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "verify_code").send_keys("8888")
# driver.find_element(By.NAME, "sbtbutton").click()

# # 登录完成再次点击去结算按钮
# time.sleep(1)
# driver.find_element(By.CLASS_NAME, "paytotal").click()

# 提交订单
time.sleep(1)
driver.find_element(By.ID, "submit_order").click()

# 确认支付方式
time.sleep(4)
driver.find_element(By.LINK_TEXT, "确认支付方式").click()
# 断言订单是否成功
# time.sleep(1)
assert "订单提交成功" in driver.page_source
if "订单提交成功" in driver.page_source:
    print("订单提交成功")

# 查看我的订单
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "body > div.top-hander > div > ul > li:nth-child(1) > a").click()

#切换窗口
driver.switch_to.window(driver.window_handles[1])

# 截图运行结果
driver.get_screenshot_as_file("../result_img/order_add.png")


quit_driver(driver)
