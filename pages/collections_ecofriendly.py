from selenium.webdriver import ActionChains

from locators.ecofriendlyLocetors import EcofriendlyLocetors
from pages.base_page import BasePage


class EcoFriendly(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_counter_items_on_page(self):
        items = self.find_all(EcofriendlyLocetors.item_card)
        assert len(items) == 13

    def change_type_view(self):
        mode = self.find_all(EcofriendlyLocetors.change_mode)
        self.click_web_elemnts(mode[0])

    def cursor_move_to_first_element_of_list_and_go_item(self, locator: tuple):
        element = self.find_all(locator)[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()