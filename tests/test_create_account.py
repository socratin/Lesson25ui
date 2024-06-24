from locators.create_account import CreateAccountLocators


def test_open_page_create_new_account(create_account_page):
    create_account_page.open_page()
    assert create_account_page.find(CreateAccountLocators.field_name_page)


def test_invalid_input_email(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_email("invalid_email")
    create_account_page.click_element(CreateAccountLocators.button_create_new_account)
    assert create_account_page.find(CreateAccountLocators.error_email)


def test_invalid_input_password(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_password("123")
    create_account_page.click_element(CreateAccountLocators.button_create_new_account)
    assert create_account_page.find(CreateAccountLocators.error_password)
