from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/'

def go_to_login_page(browser):
    login_link = browser.find_element(By.ID, 'login_link')
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(url)
    go_to_login_page(browser)