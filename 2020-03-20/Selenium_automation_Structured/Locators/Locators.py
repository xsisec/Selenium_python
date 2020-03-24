from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Locators:

    def check_exists_by_xpath(xpath) :
        try :
            webdriver.find_element_by_xpath(xpath)
        except NoSuchElementException :
            return False
        return True