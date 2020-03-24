from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utils.TakeScreenShot import save_screenshot_picture


class AboutUsPageLocators(object) :
    about_us_footer_btn = (By.XPATH, "//a[contains(text(),'About us')]")