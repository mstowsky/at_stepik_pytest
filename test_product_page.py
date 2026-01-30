import time
from .pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_be_product_added_message()
    page.added_product_name_should_be_equal_product_name()
    page.cart_price_message_should_be_equal_product_price()