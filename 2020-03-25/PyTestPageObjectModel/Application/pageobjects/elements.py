import traceback

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from Application.utils.generiv_page import BasePage


def __getattr__(self, what) :
    try :
        if what in self.locator_dictionary.keys() :
            try :
                element = WebDriverWait(self.browser, self.timeout).until(
                    EC.presence_of_element_located(self.locator_dictionary[what])
                )
            except(TimeoutException, StaleElementReferenceException) :
                traceback.print_exc()

            try :
                element = WebDriverWait(self.browser, self.timeout).until(
                    EC.visibility_of_element_located(self.locator_dictionary[what])
                )
            except(TimeoutException, StaleElementReferenceException) :
                traceback.print_exc()
            # I could have returned element, however because of lazy loading, I am seeking the element before return
            return self.find_element(*self.locator_dictionary[what])
    except AttributeError :
        super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what) :
        print("No %s here!" % what)