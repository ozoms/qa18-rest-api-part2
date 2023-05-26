from selene import have, be
from selene.support.shared import browser

from tests.conftest import LOGIN, PASSWORD, WEB_URL_DEMOSHOP

browser.config.base_url = WEB_URL_DEMOSHOP


def test_login(demoshop_management):
    demoshop_management.open('')

    demoshop_management.element('.account').should(have.text(LOGIN))


def test_customer_info(demoshop_management):
    demoshop_management.open('customer/info')

    demoshop_management.element(f'[value="{LOGIN}"]').should(be.visible)


def test_cart(demoshop_management):
    demoshop_management.open('cart')

    demoshop_management.element('.product-name').should(have.text('Computing and Internet'))


def test_catalog_books(demoshop_management):
    demoshop_management.open('books')

    demoshop_management.element('.page-title').should(have.text('Books'))
