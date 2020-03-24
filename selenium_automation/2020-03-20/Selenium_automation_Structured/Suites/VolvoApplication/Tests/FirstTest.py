import logging

from Suites.VolvoApplication.Tests.welcome import WelcomePage
from Utility.drivermanager import DriverManager
from Utility.services import Services


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)




class ChallengingDomPageTest(DriverManager):
    def test_challenging_dom_page(self):
        welcome_page = WelcomePage(self.driver)
        btn_lst = welcome_page.verify_welcome_page().click_on_link("Challenging DOM").get_list_of_all_buttons()

