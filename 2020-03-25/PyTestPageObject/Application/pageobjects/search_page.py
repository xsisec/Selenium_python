from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class DuckDuckGoSearchPage :
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser) :
        self.browser = browser

    def load(self, base_url) :
        self.browser.get(base_url)

    def search(self) :
        PHRASE = 'panda'
        search_input = self.driver.find_element_by_id('search_form_input_homepage')
        search_input.send_keys(PHRASE + Keys.RETURN)
