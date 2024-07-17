import time

from selenium import webdriver


def get_chromeDriver(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver


def quit_driver(driver):
    time.sleep(3)
    driver.quit()
