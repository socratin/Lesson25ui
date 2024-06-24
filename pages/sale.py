from locators.SaleLocetors import SaleLocators
from pages.base_page import BasePage


class Sale(BasePage):
    page_url = "/sale.html"

    def choose_category_women(self, locators):
        elements = self.find_all(SaleLocators.category_hoddies_and_sweaters)
        elements[0].click()
