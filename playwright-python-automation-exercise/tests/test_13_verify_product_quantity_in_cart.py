from playwright.sync_api import expect

from pages.page_objects.home_page import HomePage
from pages.page_objects.cart_page import CartPage
from pages.page_objects.products_page import ProductsPage

def test_add_products_in_cart(home_page: HomePage, cart_page: CartPage, products_page: ProductsPage) -> None:
    home_page.load()
    expect(home_page.title).to_be_visible()
    home_page.view_product_by_position(0)
    products_page.set_quantity('4')
    products_page.add_button.click()
    products_page.continue_shopping.click()
    home_page.cart_button.click()
    expect(cart_page.get_item_quantity_by_position(0)).to_contain_text('4')