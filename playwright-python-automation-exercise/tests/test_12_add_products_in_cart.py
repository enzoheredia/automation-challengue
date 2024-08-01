from playwright.sync_api import expect

from pages.page_objects.home_page import HomePage
from pages.page_objects.products_page import ProductsPage
from pages.page_objects.cart_page import CartPage

def test_add_products_in_cart(home_page: HomePage, products_page: ProductsPage, cart_page: CartPage) -> None:
    home_page.load()
    expect(home_page.title).to_be_visible()
    home_page.products_button.click()
    expect(products_page.all_products).to_have_text('All Products')
    products_page.search_product('blue top')
    products_page.add_product_to_cart()
    products_page.continue_shopping.click()
    products_page.search_product('men Tshirt')
    products_page.add_product_to_cart()
    products_page.continue_shopping.click()
    home_page.cart_button.click()
    expect(cart_page.get_item_price_by_position(0)).to_contain_text('Rs. 500')
    expect(cart_page.get_item_price_by_position(1)).to_contain_text('Rs. 400')
    expect(cart_page.get_item_quantity_by_position(0)).to_contain_text('1')
    expect(cart_page.get_item_quantity_by_position(1)).to_contain_text('1')
    expect(cart_page.get_item_total_by_position(0)).to_contain_text('Rs. 500')
    expect(cart_page.get_item_total_by_position(1)).to_contain_text('Rs. 400')