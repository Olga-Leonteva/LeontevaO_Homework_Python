import allure
from selenium.webdriver.common.by import By


# Все данные для теста в одном словаре
"""Словарь с данными для заполнения формы"""
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


@allure.epic("Форма")
@allure.severity("major")
@allure.title("Форма для заполнения данных для оптарвления посылки")
@allure.description(
    "Проверка работы формы для заполения личных данных пользователя")
class FormPage:
    """
        Класс для заполнения данными формы,
        проверки подсвечивания окон для ввода данных"""
    @allure.step("Запустить браузер и открыть странницу для заполнения формы")
    @allure.feature("Driver")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ввести данные в форму")
    @allure.feature("Data")
    def data(self):
        # Заполнение формы
        """Функция для ввода ранее указанных данных"""
        for field, value in TEST_DATA.items():
            # Селектор для заполнения формы
            self._driver.find_element(
                By.CSS_SELECTOR, f'input[name="{field}"]').send_keys(value)

    @allure.step("Нажать кнопку Submit")
    @allure.feature("Click_button")
    def click_button(self):
        # Нажатие кнопки Submit
        """Функция нажатия кнопки Submit"""
        self._driver.find_element(By.CSS_SELECTOR, '.btn').click()

    @allure.step("Проверить подсветку окон: зеленое - верно, красное - пустое")
    @allure.feature("Test color")
    def t_color(self):
        # Проверка подсветки полей
        """
            Функция для проверки подсветки полей:
            верно - зеленый, пустое поле - красный"""
        for field in TEST_DATA.keys():
            # Селектор для проверки результата
            result_selector = f'#{field}'
            element_class = self._driver.find_element(
                By.CSS_SELECTOR, result_selector).get_attribute('class')
            if field == "zip-code":
                assert element_class == "alert py-2 alert-danger", f"Поле {
                    field} не подсвечено красным"
            else:
                assert element_class == "alert py-2 alert-success", f"Поле {
                    field} не подсвечено зеленым"

    @allure.step("Закрыть окно браузера")
    @allure.feature("Close")
    def close_driver(self):
        """Функция закрытия браузера"""
        self._driver.quit()
