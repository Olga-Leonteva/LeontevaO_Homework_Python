from selenium.webdriver.common.by import By
import allure


@allure.epic("Магазин")
@allure.severity("major")
@allure.title("Проверка суммы для оплаты покупок")
@allure.description(
    "Проверка работы алгоритма по совершению покупок в олнлайн магазине")
class ShopResultPage:
    """Класс для вывода стоимости покупок"""
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Получить стоимость покупок")
    @allure.feature("Result Shop")
    def shop_result(self):
        """Функция для вывода стоимости покупок"""
        total = self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
        return total

    @allure.step("Закрыть браузер")
    @allure.feature("Close")
    def close_shop(self):
        """Функция закрытия браузера"""
        self.driver.quit()
