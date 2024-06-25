from locators.SaleLocetors import SaleLocators
from pages.base_page import BasePage


class Sale(BasePage):
    page_url = "/sale.html"

    def choose_category_women_hoddies_and_sweaters(self):
        elements = self.find_all(SaleLocators.category_hoddies_and_sweaters)
        elements[0].click()

    def check_visible_all_category(self):
        assert len(self.find_all(SaleLocators.name_category)) == 3

    def check_visible_block_promo(self):
        assert self.find(SaleLocators.block_promo)