import time
import pytest
from .pages.product_page import ProductPage

#url1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#url2 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'

url_src = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
url_offer = '?promo=offer'
url_offers_list = []
# Формируем список ссылок вида
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offerN
# где вместо N будут цифры от 0 до 9 включительно
for i in range(10):
    url_offers_list.append(url_src+url_offer+str(i))

@pytest.mark.parametrize('url', url_offers_list)
def test_guest_can_add_product_to_basket(browser, url):
    print(f'Start test for offer: {url[-6:]}')
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_be_product_added_message()
    page.added_product_name_should_be_equal_product_name()
    page.cart_price_message_should_be_equal_product_price()