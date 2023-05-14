from selene import have, be
from selene.support.shared import browser

from tests.conftest import LOGIN, PASSWORD, WEB_URL_DEMOSHOP

browser.config.base_url = WEB_URL_DEMOSHOP


def test_login(demoshop_management):
    browser.open('')

    browser.element('.account').should(have.text(LOGIN))


def test_customer_info(demoshop_management):
    browser.open('customer/info')

    browser.element(f'[value="{LOGIN}"]').should(be.visible)


def test_cart(demoshop_management):
    browser.open('cart')

    browser.element('.product-name').should(have.text('Computing and Internet'))


def test_catalog_books(demoshop_management):
    browser.open('books')

    browser.element('.page-title').should(have.text('Books'))
