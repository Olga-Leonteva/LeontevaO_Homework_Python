from selenium.webdriver.common.by import By
from config import b_url
import allure


@allure.epic("Калькулятор")
@allure.severity("major")
@allure.title("Выполнение действия сложения на калькулаторе")
@allure.description(
    "Проверка работы калькулатора: 7+8=; ожидание результата 45 секунд")
class Data_calc:
    """
        Класс для настройки времени ожидания выполнения вычисления,
        нажатия заданных кнопок на калькуляторе
        """
    @allure.step("Запустить браузер и открыть окно Калькулятор")
    @allure.feature("Driver")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(b_url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    # Время ожидания 45
    @allure.step("Настроить таймер ожидания на 45 секунд")
    @allure.feature("Timer")
    def timer(self):
        """Функция для настройки таймера ожидания выполнения вычисления"""
        delay = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay.clear()
        delay.send_keys("45")

    # Нажать 7 + 8
    @allure.step("Нажать на кальляторе кнопки")
    @allure.feature("Click button 7+8")
    def cluck_button_calc(self):
        """Функция нажатия кнопок на калькуляторе 7+8"""
        with allure.step("Нажать 7"):
            self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        with allure.step("Нажать +"):
            self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        with allure.step("Нажать 8"):
            self._driver.find_element(By.XPATH, "//span[text()='8']").click()
