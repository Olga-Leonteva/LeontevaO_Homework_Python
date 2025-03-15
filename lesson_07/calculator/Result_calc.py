from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Result_calc:
    def __init__(self, browser):
        self._driver = browser

    def click_equals(self):
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result_calculator(self):
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15")
            )

    def get_result(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(txt)

    def close_driver(self):
        self._driver.quit()
