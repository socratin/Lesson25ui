from locators.create_account import CreateAccountLocators
from pages.base_page import BasePage


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"

    def fill_email(self, email):
        self.find(CreateAccountLocators.input_email).send_keys(email)

    def fill_password(self, password):
        self.find(CreateAccountLocators.input_password).send_keys(password)

