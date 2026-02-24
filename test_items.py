import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    
    # Даем время рецензенту визуально проверить язык кнопки
    time.sleep(30)
    
    # Ищем кнопку по селектору
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что кнопка нашлась
    assert len(buttons) > 0, "Кнопка добавления в корзину не найдена!"
