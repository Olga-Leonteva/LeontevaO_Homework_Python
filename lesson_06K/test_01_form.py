from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.test_01
def test_form():
    driver = webdriver.Chrome()

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html.
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Заполните форму значениями
    f_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    f_name.send_keys("Иван")

    l_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    l_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")

    num = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    num.send_keys("+7985899998787")

    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")

    job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")

    # Нажмите кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, '.btn').click()

    # Проверьте (assert), что поле Zip code подсвечено красным.
    t_zip_code = driver.find_element(
        By.CSS_SELECTOR, '#zip-code').get_attribute('class')
    assert t_zip_code == ("alert py-2 alert-danger"), "Баг"

    # Проверьте (assert), что остальные поля подсвечены зеленым.
    t_f_name = driver.find_element(
        By.CSS_SELECTOR, '#first-name').get_attribute('class')
    assert t_f_name == ("alert py-2 alert-success"), "Баг"

    t_l_name = driver.find_element(
        By.CSS_SELECTOR, '#last-name').get_attribute('class')
    assert t_l_name == ("alert py-2 alert-success"), "Баг"

    t_address = driver.find_element(
        By.CSS_SELECTOR, '#address').get_attribute('class')
    assert t_address == ("alert py-2 alert-success"), "Баг"

    t_email = driver.find_element(
        By.CSS_SELECTOR, '#e-mail').get_attribute('class')
    assert t_email == ("alert py-2 alert-success"), "Баг"

    t_num = driver.find_element(
        By.CSS_SELECTOR, '#phone').get_attribute('class')
    assert t_num == ("alert py-2 alert-success"), "Баг"

    t_city = driver.find_element(
        By.CSS_SELECTOR, '#city').get_attribute('class')
    assert t_city == ("alert py-2 alert-success"), "Баг"

    t_country = driver.find_element(
        By.CSS_SELECTOR, '#country').get_attribute('class')
    assert t_country == ("alert py-2 alert-success"), "Баг"

    t_job = driver.find_element(
        By.CSS_SELECTOR, '#job-position').get_attribute('class')
    assert t_job == ("alert py-2 alert-success"), "Баг"

    t_company = driver.find_element(
        By.CSS_SELECTOR, '#company').get_attribute('class')
    assert t_company == ("alert py-2 alert-success"), "Баг"

    # Закрытие браузера
    driver.quit()
