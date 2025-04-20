from selenium.webdriver.common.by import By
from config_UI import UI_URL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Kinopoisk_UI:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get(UI_URL)

    def title_home_page(self):
        title = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.kinopoisk-header-logo__img')))
        title.get_attribute('alt')
        return title

    def quick_search(self):
        film = self._driver.find_element(
            By.CSS_SELECTOR, '[name="kp_query"]').send_keys(
                "Мастер и Маргарита")
        return film

    def button_login(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.styles_loginButton__LWZQp').click()
        self._driver.implicitly_wait(5)

    def number(self):
        button_login = self._driver.find_element(
            By.CSS_SELECTOR, '.passp-add-account-page-title').text
        return button_login

    def film_free(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.style_buttonLight____6ma').click()
        self._driver.implicitly_wait(5)

    def page_login(self):
        page_l = self._driver.find_element(
            By.CSS_SELECTOR, '.passp-add-account-page-title').text
        return page_l

    def button_magnifying_glass(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.search-form-submit-button__icon').click()
        self._driver.implicitly_wait(5)

    def random_seach(self):
        file = self._driver.find_element(By.CSS_SELECTOR, '#search').click()
        file.self._driver.save_screenshot("./ya.png")
