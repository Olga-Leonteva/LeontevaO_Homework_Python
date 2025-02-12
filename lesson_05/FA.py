from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith
name = '[name="username"]'
search_box = driver.find_element(By.CSS_SELECTOR, name)
search_box.send_keys("tomsmith")

sleep(5)

# В поле password введите значение SuperSecretPassword!
name = '[name="password"]'
search_box = driver.find_element(By.CSS_SELECTOR, name)
search_box.send_keys("SuperSecretPassword!")

sleep(5)

# Нажмите кнопку Login
button = '[class="fa fa-2x fa-sign-in"]'
driver.find_element(By.CSS_SELECTOR, button).click()

sleep(10)
