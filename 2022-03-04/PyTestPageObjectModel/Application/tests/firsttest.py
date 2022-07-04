import pytest
from selenium import webdriver
from Application.utils.basetest import TestSetup
from Application.pageobjects.Women_page import woman_page_helper


def test_make_search(TestSetup):
    woman_page = woman_page_helper(TestSetup)
    woman_page.go_to_site()
    woman_page.click_on_woman_btn()
    #woman_page.take_screenshot()


