import time

import pytest
from _pytest.main import Failed
from pypom import Page
from selenium.common.exceptions import NoSuchElementException

# from Application.locators.locators import AboutUsPageLocators
from selenium.webdriver.common.by import By

from Application.locators.locators import AboutUsPageLocators


class About_Us_Page(Page) :

    def __init__(self, driver) :
        self.AboutUsPageLocator = AboutUsPageLocators
        super().__init__(driver)

    def click_on_about_us(self) :
        self.find_element(*self.AboutUsPageLocator.about_us_footer_btn).click()
        time.sleep(2)
        pytest.fail()


        # self.find_element(*self.about_us_locator.about_us_footer_btn).click()
