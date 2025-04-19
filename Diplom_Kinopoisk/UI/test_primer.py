from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


# Проверка заголовка на главной странице
@pytest.mark.test_01
def test_home_page():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.kinopoisk.ru/')
    driver.implicitly_wait(4)
    driver.maximize_window()

    title_hp = driver.find_element(
        By.CSS_SELECTOR, '.kinopoisk-header-logo__img').get_attribute('alt')
    assert title_hp == ('Кинопоиск'), 'Баг'

    driver.quit()


# Быстрый поиск фильма
@pytest.mark.test_02
def test_quick_search():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.kinopoisk.ru/')
    driver.implicitly_wait(4)
    driver.maximize_window()

    # Ввод названия фильма "Мастер и Маргарита" в окно поиска
    film = driver.find_element(By.CSS_SELECTOR, '[name="kp_query"]')
    film.send_keys("Мастер и Маргарита")

    seach_film = driver.find_element(
        By.CSS_SELECTOR, '#suggest-item-film-1115471').text
    assert seach_film == ("Мастер и Маргарита"), 'Баг'


# Вход в личный кабинет
@pytest.mark.test_03_ui
def test_button_login():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.kinopoisk.ru/')
    driver.implicitly_wait(10)

    # Нажать кнопку "Войти"
    driver.find_element(By.CSS_SELECTOR, '.styles_loginButton__LWZQp').click()
    driver.implicitly_wait(5)

    button_login = driver.find_element(
        By.CSS_SELECTOR, '.passp-add-account-page-title').text
    assert button_login == ("Введите номер телефона")


# Смотреть кино бесплатно
@pytest.mark.test_04_ui
def test_film_reee():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.kinopoisk.ru/')
    driver.implicitly_wait(10)

    # Нажать кнопку "Смотреть кино бесплатно"
    driver.find_element(By.CSS_SELECTOR, '.style_buttonLight____6ma').click()
    driver.implicitly_wait(5)

    page_login = driver.find_element(
        By.CSS_SELECTOR, '.passp-add-account-page-title').text
    assert page_login == ("Введите номер телефона")


# Случайный поиск
@pytest.mark.test_05_ui
def test_random_seach():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.kinopoisk.ru/')
    driver.implicitly_wait(10)

    # Нажать кнопку "Лупа"
    driver.find_element(
        By.CSS_SELECTOR, '.search-form-submit-button__icon').click()
    driver.implicitly_wait(5)

    driver.find_element(By.CSS_SELECTOR, '#search').click()
    driver.save_screenshot("./ya.png")
    driver.quit()
