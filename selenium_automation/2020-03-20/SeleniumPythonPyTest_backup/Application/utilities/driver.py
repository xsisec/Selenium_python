from selenium import webdriver
import pytest
import datetime,os

#from utilities import CaptureScreen
#from pageobjects.cookies_page import cookies_window

from testdata.testdata import google_url,test_environment_url,juiceshop_url


@pytest.fixture()
def environment_setup():
    global driver
    driver = webdriver.Chrome()
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    driver.get(juiceshop_url())
    ''''for filenames'''
    global date_stamp
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    global file_name
    file_name=date_stamp + ".png"

    yield
    driver.close()

