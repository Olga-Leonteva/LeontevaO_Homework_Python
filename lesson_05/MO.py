from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/entry_ad")

continue_link = driver.find_element_by_link_text('Close').clik()

sleep(10)
