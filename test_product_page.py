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

# Записываем заранее известные баги, чтобы проставить им пометку xfail
xfail_list = ['offer7']

@pytest.mark.parametrize('url', url_offers_list)
def test_guest_can_add_product_to_basket(browser, url):
    print(f'Start test for offer: {url[-6:]}')

    # Если ссылка из списка известных багов, то проставляем метку xfail
    for i in xfail_list:
        if i in url:
            pytest.xfail(f'Known bug in page \'{i}\'')

    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_be_product_added_message()
    page.added_product_name_should_be_equal_product_name()
    page.cart_price_message_should_be_equal_product_price()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url_src)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url_src)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, url_src)
    page.open()
    cart_page = page.go_to_cart_page()
    cart_page.cart_should_be_empty()
    cart_page.should_be_empty_cart_message()