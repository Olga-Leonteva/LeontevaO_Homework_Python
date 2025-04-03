from selenium.webdriver.common.by import By
import allure


@allure.epic("Магазин")
@allure.severity("major")
@allure.title("Данные пользователя")
@allure.description(
    "Проверка работы алгоритма по совершению покупок в олнлайн магазине")
class YourInformationPage:
    """Класс для ввода данных (имя, фамилия, индекс)"""
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Ввести данные пользователя")
    @allure.feature("You information")
    def your_information(self, f_name: str, l_name: str, code: int):
        """Функция для ввода личных данных"""
        with allure.step("Ввести имя {f_name}"):
            self.driver.find_element(
                By.CSS_SELECTOR, '#first-name').send_keys(f_name)
        with allure.step("Ввести фамилисю {l_name}"):
            self.driver.find_element(
                By.CSS_SELECTOR, '#last-name').send_keys(l_name)
        with allure.step("Ввести индекс {code}"):
            self.driver.find_element(
                By.CSS_SELECTOR, '#postal-code').send_keys(code)

    @allure.step("Нажать кнопку Continue")
    @allure.feature("Click button Continue")
    def click_continue(self):
        # Нажимаем кнопку Continue
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
