from .base_page import BasePage
from .locators import LoginPageLocators

login_string = 'login'

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.driver.current_url
        assert login_string in current_url, f'Substring \'{login_string}\' is not found in current url: {current_url}'

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'Login form is not found'

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), 'Register form is not found'