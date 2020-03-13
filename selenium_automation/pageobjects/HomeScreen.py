from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings

class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "site-title")))
        self.icon = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "custom-logo")))
        self.top_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "top-menu")))
        self.post_list = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((
                By.TAG_NAME, "article")))
        self.twitter_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[contains(text(), 'Twitter')]")))
        self.linkedin_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[contains(text(), 'LinkedIn')]")))