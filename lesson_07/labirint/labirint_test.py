from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


cookie = {"name": "cookie_policy", "value": "1"}


@pytest.mark.test_labirint
def test_card_counter():
    browser = webdriver.Chrome()
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    sleep(5)
    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    # Получить текущее значение
    # txt = browser.find_element(
    # By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(
    # By.CSS_SELECTOR, 'b').text

    # Сравнить c counter
    # assert counter == int(txt)
    browser.quit()
