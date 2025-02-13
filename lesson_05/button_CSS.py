from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")


button_class = '[class*="btn-primary"]'
driver.find_element(By.CSS_SELECTOR, button_class).click()

sleep(10)
