from selenium.webdriver.remote.webdriver import WebDriver

from locators.SaleLocetors import SaleLocators


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple):
        element = self.find(locator)
        element.click()

    def click_web_elemnts(self, web_element):
        web_element.click()

    def click_logo(self):
        self.click_element(SaleLocators.logo)

    def check_current_url(self, url):
        assert self.driver.current_url == url

    def check_title(self, title):
        assert self.driver.title == title

    def check_text_in_element(self, locator: tuple, text: str):
        element = self.find(locator)
        assert text in element.text

    def check_text_in_element_all(self, locator: tuple, text: str):
        elements = self.find_all(locator)
        for element in elements:
            assert text in element.text