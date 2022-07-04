from pypom import Page
from selenium.common.exceptions import NoSuchElementException

from Application.locators.locators import AboutUsPageLocators



class About_Us_Page(Page):
    def __init__(self, driver) :

        self.about_us_locator = AboutUsPageLocators
        super().__init__(driver)

    def click_on_about_us(self) :
        self.find_element(*self.about_us_locator.about_us_footer_btn).click()