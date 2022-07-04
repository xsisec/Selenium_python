from selenium.webdriver.common.by import By

from Application.utils.basetest import BasePage


class woman_page_locators:
    woman_btn = (By.XPATH, "//a[@class='sf-with-ul'][contains(text(),'Women')]")


class woman_page_helper(BasePage):
    def click_on_woman_btn(self):
        self.driver.find_element(By.ID, "mat-input-0").send_keys("daniel.elm.test+platformadmin@gmail.com")
        self.driver.find_element(By.ID, "mat-input-1").send_keys("Test1234!")
