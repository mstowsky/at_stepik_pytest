from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_FORM), 'It seems like the cart is not empty, some items are found.'

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), '\'Empty cart\' message is not found.'