from pageobjects.HomeScreen import HomeScreen


def test_home_screen_components(self):
    home_screen = HomeScreen(self.driver)
    home_screen.validate_title_is_present()
    home_screen.validate_icon_is_present()
    home_screen.validate_menu_options_are_present()
    home_screen.validate_posts_are_visible()
    home_screen.validate_social_media_links()