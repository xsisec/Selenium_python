from os import getcwd, path, makedirs, system
from selenium import webdriver

import pytest

from Application.pageobjects.search_page import DuckDuckGoSearchPage


@pytest.fixture()
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("http://www.svt.se")
    driver.maximize_window()

    def close_driver():
        driver.quit()
    request.addfinalizer(close_driver)
    return driver


@pytest.fixture()
def get_welcome_page(get_driver):
    page = DuckDuckGoSearchPage(get_driver)
    page.search()
