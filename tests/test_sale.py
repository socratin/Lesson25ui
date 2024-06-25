from locators.SaleLocetors import SaleLocators


def test_choose_woomen_deals_category(create_sale_page):
    create_sale_page.open_page()
    create_sale_page.choose_category_women_hoddies_and_sweaters()
    create_sale_page.check_visible_all_category()

def test_go_ti_main_page(create_sale_page):
    create_sale_page.open_page()
    create_sale_page.click_logo()
    create_sale_page.check_current_url("https://magento.softwaretestingboard.com/")


def test_view_promo_block(create_sale_page):
    create_sale_page.open_page()
    create_sale_page.check_visible_block_promo()
