from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button = '[class="btn btn-primary"]'
driver.find_element(By.CSS_SELECTOR, button).click()

sleep(10)
