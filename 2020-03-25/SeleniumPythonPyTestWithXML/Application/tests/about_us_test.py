import os
import unittest
import time
from datetime import datetime

import sys
from io import StringIO

import pytest
import xmlrunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from xmlrunner import XMLTestRunner

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
        self.stream = StringIO()
        self.fake_stream = StringIO()
        self.runner = xmlrunner.XMLTestRunner(output=self.stream, stream=self.fake_stream, elapsed_times=False)

    def test_page_load(self) :
        global test_method_name
        test_method_name = self._testMethodName
        print("\n" + str(test_cases(0)))
        page = About_Us_Page(self.driver)
        page.click_on_about_us()

    def tearDown(self) :
        self.driver.close()





if __name__ == "__main__" :
    #current_directory = os.getcwd()
    suite = unittest.TestLoader().loadTestsFromTestCase(Testpages)
    #xmlrunner.XMLTestRunner(output='../../Application/Reports/reports/').run(suite)
    #timestamp = time.strftime('%Y_%m_%d_%H_%M')
    #file_name = 'Test_Report_' + test_method_name + '.xml'
    #my_dir = "../../Application/Reports/reports/"
    #result = XMLTestRunner(my_dir + file_name, "w")
    #result.run(suite)


   # testRunner = xmlrunner.XMLTestRunner(output='reports')


