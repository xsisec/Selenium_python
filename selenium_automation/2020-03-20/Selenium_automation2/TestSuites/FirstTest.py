import logging
import unittest

from PageObjects.pageobjects import HTMLElement
from Utility.drivermanager import DriverManager
from Helpers import locators
from PageObjects import Our_stock_page

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class MyFirstTest(DriverManager):
    def firstMethod(self):
        welcome_page = self.driver
        welcome_page.get("http://www.svt.se")



if __name__ == "__main__" :
    unittest.main()