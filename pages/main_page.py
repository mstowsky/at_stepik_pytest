from selenium.webdriver.common.by import By

from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.driver.find_element(By.ID, 'login_link')
        login_link.click()

    def should_be_login_link(self):
        self.driver.find_element(By.ID, 'login_link_invalid') #на данном этапе специально указан неверный селектор login_link_invalid