from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    ADDED_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-of-type(1)')
    ADDED_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-of-type(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'article[class="product_page"] h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-info strong')