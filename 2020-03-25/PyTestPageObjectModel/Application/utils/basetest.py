import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Application.utils.environments import StoreAppExample
import os
from Application.utils.take_screenshot import save_screenshot_picture


class BasePage :

    def __init__(self, driver) :
        self.driver = driver
        self.base_url = StoreAppExample()



    def go_to_site(self) :
        self.driver.get(self.base_url)

    def take_screenshot(self):
        save_screenshot_picture(self, self.driver)




@pytest.fixture(scope='function')  # default scope
def TestSetup(request) :
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
