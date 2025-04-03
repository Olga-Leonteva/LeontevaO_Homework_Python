from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Калькулятор")
@allure.severity("major")
@allure.title("результат действия сложения на калькулаторе")
@allure.description(
    "Проверка работы калькулатора: 7+8=; ожидание результата 45 секунд")
class Result_calc:
    """В этом классе осуществляется проверка результата"""
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Нажать =")
    @allure.feature("Click button =")
    def click_equals(self):
        """Функция нажатия кнопки ="""
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Подаждать результата: 15")
    @allure.feature("Result_calculator")
    def result_calculator(self):
        """Функция ожидания результата"""
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15")
            )

    @allure.step("Получить результат (15) и перевести str в int")
    @allure.feature("Result str->int")
    def get_result(self):
        """Функция получения результата и перевода в числительное"""
        txt = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(txt)

    @allure.step("Закрыть окно браузера")
    @allure.feature("Close")
    def close_driver(self):
        """Функция закрытия браузера"""
        self._driver.quit()
