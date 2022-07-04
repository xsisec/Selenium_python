import logging

from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


def click_on_xpath(self, locator):
    """
    This method is get the text present within given web element.

    param locator: XPATH of given element
    param_type: string
    """

    return self.driver.find_element_by_xpath(locator).click()
