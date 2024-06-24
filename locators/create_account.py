from selenium.webdriver.common.by import By


class CreateAccountLocators:
    field_name_page = (By.XPATH, "//span[text()='Create New Customer Account']")

    input_email = (By.ID,  "email_address")
    input_password  =  (By.ID,  "password")

    button_create_new_account = (By.XPATH, "//button[@class='action submit primary']")

    error_email = (By.ID, "email_address-error")
    error_password   =  (By.ID,  "password-error")