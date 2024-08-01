from playwright.sync_api import Page

from pages.locators.products_page_locators import ProductsPageLocators
from pages.page_objects.base_page import BasePage
from pages.elements import TextInput

class ProductsPage(BasePage):
    URL = '/'
    search_input = TextInput(ProductsPageLocators.SEARCH_INPUT)
    quantity = TextInput(ProductsPageLocators.QUANTITY)

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.all_products = self.page.locator(ProductsPageLocators.ALL_PRODCUCTS)
        self.submit_search = self.page.locator(ProductsPageLocators.SUBMIT_SEARCH)
        self.single_product = self.page.locator(ProductsPageLocators.SINGLE_PRODUCT)
        self.add_to_cart = self.page.locator(ProductsPageLocators.ADD_TO_CART).first
        self.continue_shopping = self.page.locator(ProductsPageLocators.CONTINUE_SHOPPING)
        self.add_button = self.page.locator(ProductsPageLocators.ADD_BUTTON)
    
    def search_product(self, search_query: str) -> None:
        self.search_input = search_query
        self.submit_search.click()

    def add_product_to_cart(self) -> None:
        self.single_product.hover()
        self.add_to_cart.click()

    def set_quantity(self, quantity: str) -> None:
        self.quantity = quantity