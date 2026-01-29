import time
from .pages.main_page import MainPage

url = 'http://selenium1py.pythonanywhere.com/'

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    time.sleep(2)

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()
    time.sleep(2)