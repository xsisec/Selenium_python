import unittest
import xmlrunner
from selenium import webdriver
import datetime
from Application.pageobjects.about_us_page import AboutUsPage
from Application.testdata.environments import testingworld
from Application.testsuites.TestSuite import test_cases
import os
import time


class TestPages(unittest.TestCase) :

    def setUp(self) :

        self.driver = webdriver.Chrome()
        self.driver.get(testingworld())
        self.driver.minimize_window()

    def test_page_load(self) :
        print("\n" + str(test_cases(0)))
        page = AboutUsPage(self.driver)
        page.click_sign_in_button()

    def tearDown(self) :
        self.driver.close()


if __name__ == "__main__" :
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner().run(suite)
