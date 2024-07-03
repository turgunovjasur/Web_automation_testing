from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        var = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        var.click()

    def enter_data(self, locator, text):
        var = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        var.send_keys(text)

    def get_element_text(self, locator):
        var = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return var.text

    def is_element_visible(self, locator):
        var = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return bool(var)

    def clear_field(self, locator):
        var = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        var.clear()
