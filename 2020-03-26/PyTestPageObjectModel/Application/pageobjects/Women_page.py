from selenium.webdriver.common.by import By

from Application.utils.basetest import BasePage


class woman_page_locators:
    woman_btn = (By.XPATH, "//a[@class='sf-with-ul'][contains(text(),'Women')]")


class woman_page_helper(BasePage):


    def click_on_woman_btn(self):
        self.find_element(woman_page_locators.woman_btn, time=1).click()

