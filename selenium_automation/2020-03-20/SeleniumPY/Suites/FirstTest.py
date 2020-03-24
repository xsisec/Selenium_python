
import unittest

from Utility.base_test import BaseTest
from TestData.TestData import TestData

class Test(BaseTest,unittest.TestCase):
    def __init__(self,driver,base_url):
        super(Test, self).__init__(driver, TestData.TEST_ENVIRONMENT_URL)


    def run(self):

        driver= self.driver.get()

        self.driver.close()