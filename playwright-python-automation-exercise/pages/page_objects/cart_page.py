from playwright.sync_api import Page


from pages.page_objects.base_page import BasePage
from pages.locators.cart_page_locators import CartPageLocators

class CartPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
    
    def get_item_price_by_position(self, position: int) -> None:
        self.item_price = self.page.locator(CartPageLocators.ITEM_PRICE).nth(position)
        return self.item_price
    
    def get_item_quantity_by_position(self, position: int) -> None:
        self.item_quantity = self.page.locator(CartPageLocators.ITEM_QUANTITY).nth(position)
        return self.item_quantity
    
    def get_item_total_by_position(self, position: int) -> None:
        self.item_total = self.page.locator(CartPageLocators.ITEM_TOTAL).nth(position)
        return self.item_total
    
# the 3 functions to return items can be refactored to be only one and pass column as parameter, didn't do it for lack of time