
from Utility.drivermanager import DriverManager


class WelcomePage() :
    def test_welcomepage(self) :
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()




class WelcomePageTest(DriverManager):
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()