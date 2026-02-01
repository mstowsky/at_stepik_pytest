from pages.login_page import LoginPage

url = 'http://selenium1py.pythonanywhere.com/accounts/login/'

def test_guest_can_see_login_form(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()

def test_login_link_is_correct(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()