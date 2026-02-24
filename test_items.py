import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Оставляем браузер открытым на 30 секунд для визуальной проверки языка (по условию задания)
    # time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    # Используем селектор, который однозначно находит кнопку
    add_to_basket_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что список кнопок не пуст
    assert len(add_to_basket_buttons) > 0, "Button 'Add to basket' not found on the page!"
