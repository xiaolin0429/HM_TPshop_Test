import time

from selenium import webdriver


def get_EdgeDriver(url):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    return driver


def quit_driver(driver):
    time.sleep(3)
    driver.quit()
