from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


add_element = '[onclick="addElement()]'
seach_add = driver.find_element(By.CSS_SELECTOR, add_element)

for add in range(5):
    seach_add.click()

delete = '.add_manually'

print(len(driver.find_elements(By.CSS_SELECTOR, delete)))

sleep(5)
