from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith
name = "username"
search_box = driver.find_element(By.ID, name)
search_box.send_keys("tomsmith")

sleep(5)

# В поле password введите значение SuperSecretPassword!
pas = "password"
search_box = driver.find_element(By.ID, pas)
search_box.send_keys("SuperSecretPassword!")

sleep(5)

# Нажмите кнопку Login
button = ".fa-sign-in"
driver.find_element(By.CSS_SELECTOR, button).click()

sleep(10)
