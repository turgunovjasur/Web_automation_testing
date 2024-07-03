from navigations.signup_navigation import LoginNavigation


class LoginActions(LoginNavigation):

    def login_actions(self, email, password):
        self.navigate_sign_up_page()
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        # self.click_on_agree_mark_box()
        # self.click_on_start_for_free_button()
        self.click_on_create_qase_account()
        assert self.is_congratulation_exist(), "Sign up was not successful!"
        assert self.is_email_container_shows_entered_email(email)
        return True