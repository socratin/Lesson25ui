from selenium.webdriver.common.by import By


class EcofriendlyLocetors:
    item_card = (By.XPATH, "//div[@class='product-item-info']")
    change_mode = (By.XPATH, "//a[@id='mode-list']")

    field_amount_items = (By.ID,  "toolbar-amount")

    items_list = (By.XPATH,  "//li[@class='item product product-item']")

class CardItem:
    item_name = (By.XPATH, "//span[@class='base']")