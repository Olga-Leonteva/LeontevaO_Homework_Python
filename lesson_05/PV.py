from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/inputs")

# ввести в проле текст 1000
num = '[type="number"]'
search_box = driver.find_element(By.CSS_SELECTOR, num)
search_box.send_keys("1000")

sleep(5)

# очистить поле ввода
driver.find_element(By.CSS_SELECTOR, num).clear()

sleep(5)

# ввести в поле ввода текст 999
search_box = driver.find_element(By.CSS_SELECTOR, num)
search_box.send_keys("999")

sleep(10)
