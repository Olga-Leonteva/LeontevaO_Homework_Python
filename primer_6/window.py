from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://labirint.ru/")
driver.set_window_size(1000, 600)

sleep(10)
driver.quit()
