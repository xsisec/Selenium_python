import pytest
from selenium import webdriver


def SetUp(self,base_url):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)