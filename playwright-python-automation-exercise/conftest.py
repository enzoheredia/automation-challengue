import pytest
from playwright.sync_api import Page

from pages.page_objects.home_page import HomePage
from pages.page_objects.products_page import ProductsPage
from pages.page_objects.cart_page import CartPage
from pages.page_objects.products_page import ProductsPage

@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }

@pytest.fixture()
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture()
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture()
def cart_page(page: Page):
    return CartPage(page)