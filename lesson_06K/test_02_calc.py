from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.test_02
def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Время ожидания 45
    delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay.clear()
    delay.send_keys("45")

    # Нажать 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Результат
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверка
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15

    # Закрытие браузера
    driver.quit()
