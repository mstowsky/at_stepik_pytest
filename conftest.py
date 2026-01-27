import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='You need to specify a browser, for example \'chrome\' or \'firefox\'')
    parser.addoption('--language', action='store', default='en',
                     help='You need to specify a language, for example \'ru\' or \'en\'')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    print(f'\n--- Start browser: {browser_name}, language: {user_language} ---')
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_language': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('Parameter \'--browser\' should be \'chrome\' or \'firefox\'')
    yield browser
    print('\n--- Stop browser ---')
    browser.quit()