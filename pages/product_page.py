from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_product_added_message(self):
        assert self.is_element_presented(*ProductPageLocators.ADDED_TO_CART_SUCCESS_MESSAGE), '\'Product added\' message not found'

    def added_product_name_should_be_equal_product_name(self):
        added_product_name = self.driver.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT_NAME).text
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert added_product_name == product_name, f'Actual product name \'{added_product_name}\' is not equal to expected \'{product_name}\''

    def cart_price_message_should_be_equal_product_price(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price_message = self.driver.find_element(*ProductPageLocators.CART_PRICE_MESSAGE).text
        assert product_price == cart_price_message, f'Product price \'{product_price}\' is not equal to cart price \'{cart_price_message}\''