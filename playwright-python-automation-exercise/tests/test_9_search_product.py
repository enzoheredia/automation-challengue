from playwright.sync_api import expect

from pages.page_objects.home_page import HomePage
from pages.page_objects.products_page import ProductsPage


def test_search_product(home_page: HomePage, products_page: ProductsPage) -> None:
    search_term = 'Blue Top'
    home_page.load()
    expect(home_page.title).to_be_visible()
    home_page.products_button.click()
    expect(products_page.all_products).to_have_text('All Products')
    products_page.search_product(search_term)
    expect(products_page.all_products).to_have_text('Searched Products')
    expect(products_page.single_product).to_have_count(1)
    expect(products_page.single_product).to_contain_text(search_term)
    