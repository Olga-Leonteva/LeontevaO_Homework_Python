from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# Перейдите на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waiter = WebDriverWait(driver, 30)

# Дождитесь загрузки всех картинок.
content = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), "Done!"))

# Получите значение атрибута src  у 3-й картинки.
# Выведите значение в консоль.
img = driver.find_element(By.CSS_SELECTOR, "#award")
print(img.get_attribute('src'))

driver.quit()
