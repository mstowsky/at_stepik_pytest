import time
import pytest
from .pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_cant_see_product_added_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.should_not_be_product_added_message()

def test_guest_cant_see_product_added_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_product_added_message()

def test_product_added_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.product_added_message_disappeared()