from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# перейти на страницу
driver.get("http://uitestingplayground.com/ajax")

# нажать кнопку
button = "#ajaxButton"
driver.find_element(By.CSS_SELECTOR, button).click()
driver.implicitly_wait(30)

# получить текст зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# вывести его в консоль
print(txt)

driver.quit()
