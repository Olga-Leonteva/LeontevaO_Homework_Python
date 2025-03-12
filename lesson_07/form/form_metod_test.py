from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Все данные для теста в одном словаре
TEST_DATA = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "zip-code": "",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
}

browser = webdriver.Chrome()


def open_form():
    # Открытие страницы
    browser.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


def data():
    # Заполнение формы
    for field, value in TEST_DATA.items():
        # Селектор для заполнения формы
        browser.find_element(
            By.CSS_SELECTOR, f'input[name="{field}"]').send_keys(value)


def click_button():
    # Нажатие кнопки Submit
    browser.find_element(By.CSS_SELECTOR, '.btn').click()


def t_color():
    # Проверка подсветки полей
    for field in TEST_DATA.keys():
        # Селектор для проверки результата
        result_selector = f'#{field}'
        element_class = browser.find_element(
            By.CSS_SELECTOR, result_selector).get_attribute('class')
        if field == "zip-code":
            assert element_class == "alert py-2 alert-danger", f"Поле {
                field} не подсвечено красным"
        else:
            assert element_class == "alert py-2 alert-success", f"Поле {
                field} не подсвечено зеленым"


def close_driver():
    browser.quit()


@pytest.mark.test_01
def test_form():
    browser = webdriver.Chrome()
    open_form(browser)
    data()
    click_button()
    t_color()
    close_driver()
