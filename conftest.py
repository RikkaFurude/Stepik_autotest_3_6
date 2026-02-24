import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем параметр language в командную строку
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr, es, etc...")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра language
    user_language = request.config.getoption("language")
    
    # Настраиваем ChromeOptions для установки языка
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print(f"\nstart chrome browser for test with language: {user_language}...")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()