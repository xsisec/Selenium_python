from selenium import webdriver
import pytest
import datetime,os
from utlities import CaptureScreen
import time
from testdata.testdata import google_url,test_environment_url,juiceshop_url
from pageobjects.cookies_page import cookies_window

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
    driver.title



def testmethod2(environment_setup):
    driver.find_element_by_xpath(cookies_window()).click()
    CaptureScreen.screenshot(driver, file_name)
    time.sleep(1)


