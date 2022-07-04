# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


# @pytest.fixture() execute specific method before every test method
# @pytest.yield_ficture() execute specific method before & after every test method.

@pytest.fixture()
def setup():
    print("once before every method")


def testmethod1(setup):
    print("this is is test method1")


def testmethod2(setup):
    print("this is a test method2")
