from locators.create_account import CreateAccountLocators
from pages.base_page import BasePage


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"

    def fill_email(self, email):
        self.find(CreateAccountLocators.input_email).send_keys(email)

    def fill_password(self, password):
        self.find(CreateAccountLocators.input_password).send_keys(password)

    def check_view_page(self):
        assert self.find(CreateAccountLocators.field_name_page)

    def click_button_create_new_account(self):
        self.click_element(CreateAccountLocators.button_create_new_account)

    def check_error_email(self):
        assert self.find(CreateAccountLocators.error_email)

    def check_error_password(self):
        assert self.find(CreateAccountLocators.error_password)