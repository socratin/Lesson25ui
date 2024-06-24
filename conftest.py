import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.collections_ecofriendly import EcoFriendly
from pages.create_account import CreateAccount
from pages.sale import Sale


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    # sleep(3)
    return chrome_driver

@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)

@pytest.fixture()
def create_ecofriendly_page(driver):
    return EcoFriendly(driver)

@pytest.fixture()
def create_sale_page(driver):
    return Sale(driver)

