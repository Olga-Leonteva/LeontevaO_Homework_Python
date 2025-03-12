from selenium.webdriver.common.by import By


# Все данные для теста в одном словаре
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


class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def data(self):
        # Заполнение формы
        for field, value in TEST_DATA.items():
            # Селектор для заполнения формы
            self._driver.find_element(
                By.CSS_SELECTOR, f'input[name="{field}"]').send_keys(value)

    def click_button(self):
        # Нажатие кнопки Submit
        self._driver.find_element(By.CSS_SELECTOR, '.btn').click()

    def t_color(self):
        # Проверка подсветки полей
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

    def close_driver(self):
        self._driver.quit()
