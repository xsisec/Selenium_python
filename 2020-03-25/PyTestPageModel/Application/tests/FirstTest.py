from Application.pageobjects.pageobject1 import SearchHelper


def test_yandex_search(BasePage):
    yandex_main_page = SearchHelper(BasePage)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements