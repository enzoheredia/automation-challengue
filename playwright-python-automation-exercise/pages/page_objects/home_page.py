from playwright.sync_api import Page

from pages.locators.home_page_locators import HomePageLocators
from pages.page_objects.base_page import BasePage
from pages.elements import TextInput

class HomePage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = self.page.locator(HomePageLocators.TITLE)
        self.products_button = self.page.locator(HomePageLocators.PRODUCTS_BUTTON)
        self.cart_button = self.page.locator(HomePageLocators.CART_BUTTON).first

    def view_product_by_position(self, position: int) -> None:
        self.product = self.page.locator(HomePageLocators.VIEW_PRODUCT).nth(position)
        self.product.click()