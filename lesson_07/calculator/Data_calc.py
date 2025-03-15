from selenium.webdriver.common.by import By
from config import b_url


class Data_calc:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(b_url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    # Время ожидания 45
    def timer(self):
        delay = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay.clear()
        delay.send_keys("45")

    # Нажать 7 + 8 =
    def cluck_button_calc(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
