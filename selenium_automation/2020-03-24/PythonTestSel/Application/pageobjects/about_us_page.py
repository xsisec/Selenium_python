from pypom import Page

#from Application.utils.BaseTest import
from Application.locators.locators import AboutUsPageLocators
from Application.utils import BaseTest


class AboutUsPage(Page):
    def __init__(self,driver):
        base_test=BaseTest()
        self.about_us_locator=AboutUsPageLocators
        super().__init__(driver)

    def click_sign_in_button(self) :
        self.find_element(*self.about_us_locator.about_us_btn).click()
        self.find_element(*self.about_us_locator.about_us_mission_vision_btn).click()
        print(BaseTest.MyClass.__name__)

