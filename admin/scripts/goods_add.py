from selenium.webdriver.support.select import Select
from admin.tools.edgeDriver import *
from admin.tools.login import *

# 登录商城商家后台
driver = get_login()


# 点击商城功能
time.sleep(1)
driver.find_element(By.LINK_TEXT, "商城").click()

# 点击商品
time.sleep(1)
driver.find_element(By.LINK_TEXT, "商品列表").click()

# 点击添加商品
time.sleep(1)
driver.switch_to.frame("workspace")
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]/a/div").click()
# driver.switch_to.default_content()

# 输入商品名称
time.sleep(1)
# driver.switch_to.frame("workspace")
driver.find_element(By.NAME, "goods_name").send_keys("iPhone 14 Pro Max")

# 选择商品分类
time.sleep(1)
select = Select(driver.find_element(By.ID, "cat_id"))
select.select_by_value("31")
time.sleep(1)
select = Select(driver.find_element(By.ID, "cat_id_2"))
select.select_by_value("32")

time.sleep(1)
select = Select(driver.find_element(By.ID, "cat_id_3"))
select.select_by_value("62")
# driver.find_element(By.ID, "cat_id").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#cat_id>[value='31']").click()
# time.sleep(1)
# driver.find_element(By.ID, "cat_id_2").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#cat_id_2>[value='32']").click()
# time.sleep(1)
# driver.find_element(By.ID, "cat_id_3").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#cat_id_3>[value='62']").click()
# time.sleep(1)

# 选择商品品牌
time.sleep(1)
driver.find_element(By.ID, "brand_id").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#brand_id>[value='1']").click()
time.sleep(1)

# 设置本店售价
time.sleep(1)
driver.find_element(By.NAME, "shop_price").send_keys("8999")

# 设置市场价
time.sleep(1)
driver.find_element(By.NAME, "market_price").send_keys("9999")

# 选择包邮
time.sleep(1)
driver.find_element(By.ID, "is_free_shipping_label_1").click()
time.sleep(1)

# 点击确定
time.sleep(1)
driver.find_element(By.ID, "submit").click()

quit_driver(driver)
