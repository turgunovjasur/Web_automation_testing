from screens.base_screen import BaseScreen
from selenium.webdriver.common.by import By


class HomeScreen(BaseScreen):
    screen_title = (By.XPATH, "//div/h1")
    start_for_free_button = (By.XPATH, "//p/following-sibling::div/a[text()='Start for free']")
    email_field = (By.XPATH, "//input[@name='email']")
    password_field = (By.XPATH, "//input[@name='password']")
    confirm_password_field = (By.XPATH, "//input[@name='passwordConfirmation']")
    create_your_qase_account = (By.XPATH, "//*[text()='Sign up with email']")
    congratulation_label = (By.XPATH, "//div/h1")
    email_container = (By.XPATH, "//div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def is_homescreen_title_exist(self):
        return self.is_element_visible(self.screen_title)

    def is_congratulation_exist(self):
        return self.is_element_visible(self.congratulation_label)

    def is_email_container_shows_entered_email(self, email):
        assert email in self.get_element_text(self.email_container), "Email does not appear!"

    def click_on_start_for_free_button(self):
        self.click(self.start_for_free_button)

    # def click_on_agree_mark_box(self):
    #     self.click(self.agree_mark_box)

    def click_on_create_qase_account(self):
        self.click(self.create_your_qase_account_button)

    def enter_password(self, password):
        self.enter_data(self.email_field, password)

    def enter_confirm_password(self, confirm_password):
        self.enter_data(self.confirm_password_field, confirm_password)

    def enter_email(self, email):
        self.enter_data(self.email_field, email)