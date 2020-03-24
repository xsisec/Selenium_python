"""
@author: XsiSec
"""
import logging
import sys

import unittest
from selenium import webdriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DriverManager(unittest.TestCase) :
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self) :
        """
        This method is to instantiate the web driver instance.
        """
        logging.info("## SETUP METHOD ##")
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get()


    def tearDown(self) :
        """
        This is teardown method.
        It is to capture the screenshots for failed test cases,
        & to remove web driver object.
        """
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0] :
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None :
            logging.info("# Removing the webdriver.")
            self.driver.quit()

    def create_ffprofile(self) :
        """
        This function is to create firefox profile.
        :return: firefox profile.
        """
        logging.info("# Setting up firefox profile.")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', os.getcwd())
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'text/csv,application/octet-stream,application/pdf,application/vnd.ms-excel')
        profile.set_preference("pdfjs.disabled", True)

        return profile


if __name__ == '__main__' :
    unittest.main()
