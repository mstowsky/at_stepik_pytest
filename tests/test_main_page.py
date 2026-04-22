import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

url = 'http://selenium1py.pythonanywhere.com/'

@pytest.mark.login
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        '''
        Гость может перейти на страницу авторизации с главной страницы
        '''
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        '''
        Гость может видеть ссылку на страницу авторизации на главной странице
        '''
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_products_in_cart_opened_from_main_page(browser):
    '''
    Гость видит пустую корзину, которая была открыта с главной страницы
    '''
    page = MainPage(browser, url)
    page.open()
    cart_page = page.go_to_cart_page()
    cart_page.cart_should_be_empty()
    cart_page.should_be_empty_cart_message()