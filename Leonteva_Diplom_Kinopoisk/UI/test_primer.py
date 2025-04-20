from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config_UI import UI_URL


@allure.epic("UI")
@allure.title("Проверка заголовка на главной странице")
@pytest.mark.test_01
def test_home_page():
    with allure.step("Открыть окно Кинопоиск"):
        driver = webdriver.Chrome()
        driver.get(UI_URL)
        driver.maximize_window()

    with allure.step("Найти заголовок страницы"):
        title_hp = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.kinopoisk-header-logo__img'))
                ).get_attribute('alt')

    with allure.step("Проверить заголовок"):
        assert title_hp == ('Кинопоиск'), 'Баг'

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Быстрый поиск фильма")
@pytest.mark.test_02
def test_quick_search():
    with allure.step("Открыть окно Кинопоиск"):
        driver = webdriver.Chrome()
        driver.get(UI_URL)
        driver.maximize_window()

    with allure.step("Ввести названия фильма Мастер и Маргарита"):
        film = WebDriverWait(driver, 15).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '[name="kp_query"]')))
        film.send_keys("Мастер и Маргарита")

    with allure.step("Просмотреть результат поиска"):
        seach_film = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#suggest-item-film-1115471'))).text

    with allure.step("Проверить поиск"):
        assert seach_film == ("Мастер и Маргарита"), 'Баг'

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Вход в личный кабинет")
@pytest.mark.test_03_ui
def test_button_login():
    with allure.step("Открыть окно Кинопоиск"):
        driver = webdriver.Chrome()
        driver.get(UI_URL)

    with allure.step("Нажать кнопку Войти"):
        login = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.styles_loginButton__LWZQp')))
        login.click()

    with allure.step("Найти заголовок страницы"):
        button_login = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text

    with allure.step("Проверить заголовок"):
        assert button_login == ("Введите номер телефона")

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Смотреть кино бесплатно")
@pytest.mark.test_04_ui
def test_film_reee():
    with allure.step("Открыть окно Кинопоиск"):
        driver = webdriver.Chrome()
        driver.get(UI_URL)

    with allure.step("Нажать кнопку Смотреть кино бесплатно"):
        film_free = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.style_buttonLight____6ma')))
        film_free.click()

    with allure.step("Найти заголовок страницы"):
        page_login = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text

    with allure.step("Проверить заголовок"):
        assert page_login == ("Введите номер телефона")

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Случайный поиск")
@pytest.mark.test_05_ui
def test_random_seach():
    with allure.step("Открыть окно Кинопоиск"):
        driver = webdriver.Chrome()
        driver.get(UI_URL)

    with allure.step("Нажать кнопку Лупа"):
        random_seach = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.search-form-submit-button__icon')))
        random_seach.click()

    with allure.step("Нажать кнопку Случайный фильм"):
        screenshot = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))
        screenshot.click()

    with allure.step("Сделать скриншот результата поиска"):
        driver.save_screenshot("./ya.png")

    with allure.step("Закрыть браузер"):
        driver.quit()
