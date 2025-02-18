from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# перейти на сайт
driver.get("http://uitestingplayground.com/textinput")

# указать в поле ввода текст SkyPro
search_box = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
search_box.send_keys("SkyPro")

# нажать синюю скнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(10)

# получить текст кнопки и вывести в консоль
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

driver.quit()
