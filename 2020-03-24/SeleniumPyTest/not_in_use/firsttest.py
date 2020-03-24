from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def makesearch(driver,base_url):
    driver.get(f'{base_url}/browse')
    sleep(3)
    search_box = driver.find_element_by_id('find-content-input')
    driver.quit()
    return 'Passed'

if __name__ == '__main__':

    # Create an instance of selenium web driver
    driver = webdriver.Chrome()

    # Run our first test!
    result = makesearch(driver, 'http://www.google.se')

    print(f'The test {result}!')