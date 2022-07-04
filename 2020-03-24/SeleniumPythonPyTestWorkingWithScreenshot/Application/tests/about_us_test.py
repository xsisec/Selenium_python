import os
import unittest
import time
from datetime import datetime

import sys
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Application.pageobjects.AboutUs_Page import About_Us_Page
from Application.tests.TestSuite import test_cases
from utils.TakeScreenShot import save_screenshot_picture
from utils.environments import StoreAppExample


class Testpages(unittest.TestCase) :

    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        base_url = StoreAppExample()
        self.driver.get(base_url)


    def test_page_load(self) :
        test_method_name = self._testMethodName
        print("\n" + str(test_cases(0)))
        page = About_Us_Page(self.driver)
        page.click_on_about_us()
        save_screenshot_picture(self, self.driver)



    def tearDown(self) :
        self.driver.close()




if __name__ == "__main__" :
    suite = unittest.TestLoader().loadTestsFromTestCase(Testpages)
    unittest.TextTestRunner().run(suite)
