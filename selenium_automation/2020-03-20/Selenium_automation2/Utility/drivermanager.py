import logging
import sys
import unittest
from selenium import webdriver
from TestData import TestData


class DriverManager(unittest.TestCase):
    """"this class is for initialize the driver instance"""

    def setUp(self) :
        """
        This method is to instantiate the web driver instance.
        """
        logging.info("## SETUP METHOD ##")
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(TestData.test_environment_url())

    def tearDown(self) :
        logging.info("##TearDown Method##")
        if sys.exc_info()[0] :
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)
            self.driver.quit()


if __name__ == '__main__' :
    unittest.main()