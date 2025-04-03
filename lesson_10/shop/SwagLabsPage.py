from selenium.webdriver.common.by import By
import allure


@allure.epic("Магазин")
@allure.severity("major")
@allure.title("Авторизация")
@allure.description(
    "Проверка работы алгоритма по совершению покупок в олнлайн магазине")
class SwagLabsPage:
    """Класс для авторизации пользователя"""
    @allure.step("Запустить браузер и открыть странницу магазина")
    @allure.feature("Driver")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Авторизоваться")
    @allure.feature("Authorization")
    def authorization(self, user_name: str, password: str):
        """Функция для ввода логина и пароля, нажатие кнопки Login"""
        with allure.step("Ввести логин {user_name}"):
            self._driver.find_element(
                By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        with allure.step("Ввести пароль {password}"):
            self._driver.find_element(
                By.CSS_SELECTOR, '#password').send_keys(password)
        with allure.step("Нажать кнопку Login"):
            self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
