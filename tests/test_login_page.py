from pages.login_page import LoginPage
import allure

url = 'http://selenium1py.pythonanywhere.com/accounts/login/'

def test_guest_can_see_login_form(browser):
    '''
    Гость может видеть форму авторизации
    '''
    page = LoginPage(browser, url)
    with allure.step('Шаг 1. Открыть страницу авторизации'):
        page.open()
    with allure.step('Шаг 2. Проверить, что страница авторизации отображается'):
        page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    '''
    Гость может видеть форму регистрации
    '''
    page = LoginPage(browser, url)
    with allure.step('Шаг 1. Открыть страницу авторизации'):
        page.open()
    with allure.step('Шаг 2. Проверить, что страница регистрации отображается'):
        page.should_be_register_form()

def test_login_link_is_correct(browser):
    '''
    Открытая сейчас страница имеет корректную ссылку на страницу авторизации
    '''
    page = LoginPage(browser, url)
    with allure.step('Шаг 1. Открыть страницу авторизации'):
        page.open()
    with allure.step('Шаг 2. Проверить, что активна ссылка на страницу авторизации'):
        page.should_be_login_url()