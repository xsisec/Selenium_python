import os
import unittest
from webdriver import Driver
from values import strings

import io
import unittest
import xmlrunner

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_DIR = './test-reports/unittest'
TEST_OUTPUT_FILE_NAME = 'unittest.xml'


class FirstTest(unittest.TestCase):
    """First Test"""

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        pass

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))