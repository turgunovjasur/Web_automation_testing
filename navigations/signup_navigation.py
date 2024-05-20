from screens.home_screen import HomeScreen


class LoginNavigation(HomeScreen):

    def navigate_sign_up_page(self):
        assert self.is_homescreen_title_exist()
        self.click_on_start_for_free_button()