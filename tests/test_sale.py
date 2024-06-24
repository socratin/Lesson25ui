from locators.SaleLocetors import SaleLocators


def test_choose_woomen_deals_category(create_sale_page):
    create_sale_page.open_page()
    create_sale_page.choose_category_women(SaleLocators.category_hoddies_and_sweaters)
    assert len(create_sale_page.find_all(SaleLocators.name_category)) == 3


def test_go_ti_main_page(create_sale_page):
    create_sale_page.open_page()
    create_sale_page.click_element(SaleLocators.logo)
    assert create_sale_page.driver.current_url == "https://magento.softwaretestingboard.com/"


def test_view_promo_block(create_sale_page):
    create_sale_page.open_page()
    assert create_sale_page.find(SaleLocators.block_promo)
