from selenium.webdriver.common.by import By
import allure


@allure.epic("Магазин")
@allure.severity("major")
@allure.title("Корзина")
@allure.description(
    "Проверка работы алгоритма по совершению покупок в олнлайн магазине")
class CartPage:
    """Класс Корзины с заказами"""
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Открыть страницу Корзина")
    @allure.feature("Driver")
    def get(self):
        """Функция для открытия страницы Корзины """
        self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажать кнопку Checkout")
    @allure.feature("Click button Checkout")
    def click_checout(self):
        """Функция нажатия кнопки Checkout"""
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
