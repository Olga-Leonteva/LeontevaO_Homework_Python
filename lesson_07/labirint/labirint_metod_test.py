from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome()


@pytest.mark.test_labirint
def open_labirint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search(term):
    # Найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def add_books():
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

        return counter


def close_driver():
    browser.quit()


def test_card_counter():
    browser = webdriver.Chrome()
    open_labirint()
    search('Python')
    added = add_books()
    close_driver()
    return added

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
