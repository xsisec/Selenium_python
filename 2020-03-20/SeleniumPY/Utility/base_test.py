from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class BaseTest(object):
    def __init__(self, driver, base_url):
        """init"""
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 30)
