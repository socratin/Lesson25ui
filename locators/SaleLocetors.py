from selenium.webdriver.common.by import By


class SaleLocators:
    category_hoddies_and_sweaters = (By.XPATH, "//a[text()='Hoodies and Sweatshirts']")
    name_category = (By.XPATH, "//span[text()='Hoodies & Sweatshirts']")

    logo = (By.XPATH, "//a[@class='logo']")

    block_promo = (By.XPATH, "//div[@class='blocks-promo']")
