from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def cart_should_be_empty(self):
        self.is_not_element_present(*CartPageLocators.ITEMS_FORM)

    def should_be_empty_cart_message(self):
        self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)