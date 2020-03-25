import pytest
from selenium.webdriver import Chrome
from Application.pageobjects.search_page import DuckDuckGoSearchPage


@pytest.fixture
def browser() :
    # Initialize ChromeDriver
    driver = Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    driver.get("http://www.google.se")

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_k(browser) :
    # Set up test case data
    PHRASE = 'panda'
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

