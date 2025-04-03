from selenium.webdriver.common.by import By
import allure


@allure.epic("Магазин")
@allure.severity("major")
@allure.title("Добавление товаров в корзину")
@allure.description(
    "Проверка работы алгоритма по совершению покупок в олнлайн магазине")
class ShopPage:
    """Класс добавления товаров в корзину"""
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Добавить товары в корзину")
    @allure.feature("Add")
    def add_products(self):
        """Функция добавления товаров в корзину, нажатие кнопок Add to cart"""
        # Добавляем товары в корзину
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
