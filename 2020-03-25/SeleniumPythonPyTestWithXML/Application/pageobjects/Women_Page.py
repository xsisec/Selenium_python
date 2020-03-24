from pypom import Page

from utils import BaseTest
from ..locators import locators
from ..locators.locators import About_page_loc


class Woman_Page(Page):
    def __init__(self,driver):
        base_test= BaseTest
        lc=About_page_loc()
        super().__init__(driver) #Inherit the driver anywhere.