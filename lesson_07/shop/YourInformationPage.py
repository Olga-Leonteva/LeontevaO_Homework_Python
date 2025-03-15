from selenium.webdriver.common.by import By


class YourInformationPage:
    def __init__(self, browser):
        self.driver = browser

    def your_information(self, f_name, l_name, code):
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(f_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(l_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(code)

    def click_continue(self):
        # Нажимаем кнопку Continue
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
