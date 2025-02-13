from time import sleep
from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/entry_ad")

continue_link = driver.find_element_by_link_text('Close').clik()

sleep(10)
