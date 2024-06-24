import time

from locators.ecofriendlyLocetors import EcofriendlyLocetors, CardItem


def test_view_card_items(create_ecofriendly_page):
    create_ecofriendly_page.open_page()
    create_ecofriendly_page.check_counter_items_on_page()

def test_count_view(create_ecofriendly_page):
    create_ecofriendly_page.open_page()
    create_ecofriendly_page.find(EcofriendlyLocetors.field_amount_items)

def test_view_button_cart_compare_like(create_ecofriendly_page):
    create_ecofriendly_page.open_page()
    create_ecofriendly_page.cursor_move_to_first_element_of_list_and_go_item(EcofriendlyLocetors.items_list)
    assert create_ecofriendly_page.find(CardItem.item_name)

