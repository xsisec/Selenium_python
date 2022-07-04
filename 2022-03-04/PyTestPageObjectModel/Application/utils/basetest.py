import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Application.utils.environments import StoreAppExample
import os
from Application.utils.take_screenshot import save_screenshot_picture
import sys
from selenium.webdriver.chrome.options import Options


class BasePage :

    def __init__(self, driver):
        self.driver = driver
        self.base_url = StoreAppExample()



    def go_to_site(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10)





    def take_screenshot(self):
        save_screenshot_picture(self, self.driver)




@pytest.fixture(scope='function')  # default scope
def test_setup(request):
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    yield driver
    #driver.quit()
