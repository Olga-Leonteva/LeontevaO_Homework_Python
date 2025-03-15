from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, browser):
        self._driver = browser

    def add_products(self):
        # Добавляем товары в корзину
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
