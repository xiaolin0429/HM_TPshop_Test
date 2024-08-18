import json
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_test_data():
    """
    加载测试数据。

    从JSON文件中加载搜索测试数据，用于测试搜索功能。

    Returns:
        返回一个元组列表，每个元组包含一个搜索关键字和预期的搜索结果。
    """
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "..", "test_data_json", "search_test_data.json")
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [(item["search_key"], item["expected_results"]) for item in data]


class TestSearch:
    """
    搜索功能的测试类。

    使用Selenium进行自动化测试，确保搜索功能按预期工作。
    """

    def setup_class(self):
        """
        在整个测试类开始前进行初始化。

        初始化WebDriver，设置窗口最大化，并设置隐式等待时间为10秒。
        """
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        """
        在整个测试类结束后进行清理。

        关闭WebDriver。
        """
        self.driver.quit()

    def setup_method(self):
        """
        在每个测试方法执行前进行初始化。

        导航到测试网站的主页。
        """
        self.driver.get("http://192.168.140.129/index.php/")

    @staticmethod
    def teardown_method():
        """
        在每个测试方法执行后进行清理。

        暂停3秒，以便观察测试结果。
        """
        time.sleep(3)

    @pytest.mark.parametrize("search_key, expected_results", load_test_data())
    def test_search(self, search_key, expected_results):
        """
        测试搜索功能。

        参数:
            search_key: 搜索关键字。
            expected_results: 预期的搜索结果。

        该测试方法使用Selenium WebDriver定位页面元素并执行搜索操作，然后验证搜索结果是否包含预期的关键字。
        """
        # 定位搜索框并输入搜索关键字
        self.driver.find_element(By.ID, "q").send_keys(search_key)

        # 点击搜索按钮
        self.driver.find_element(By.CLASS_NAME, "ecsc-search-button").click()

        # 获取所有商品名称的元素
        product_names = self.driver.find_elements(
            By.XPATH, "//div[@class='shop-list-splb p']//div[@class='shop_name2']/a")

        # 遍历所有商品名称，检查是否包含搜索关键字
        for product_name in product_names:
            assert search_key.lower() in product_name.text.lower(), \
                f"Product name '{product_name.text}' does not contain search key '{search_key}'"

