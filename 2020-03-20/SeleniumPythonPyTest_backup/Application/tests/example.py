
import time
from Application.pageobjects.cookies_page import cookies_window
from Application.utilities import CaptureScreen
from utilities.driver import environmentsetup

def testmethod2(environment_setup) :
    driver.find_element_by_xpath(cookies_window()).click()
    CaptureScreen.screenshot(driver, "tes")
    time.sleep(1)
