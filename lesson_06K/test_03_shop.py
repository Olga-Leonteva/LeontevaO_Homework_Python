from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
# Откройте сайт магазина: https://www.saucedemo.com/.
driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user
u_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
u_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("secret_sauce")

login = driver.find_element(By.CSS_SELECTOR, '#login-button').click()

# Добавьте в корзину товары:Sauce Labs Backpack, Sauce Labs Bolt T-Shirt,
# Sauce Labs Onesie.
button_SLB = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

button_SLBT = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

button_SLO = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

# Перейдите в корзину.
basket = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

# Нажмите Checkout.
checkout = driver.find_element(By.CSS_SELECTOR, '#checkout').click()

# Заполните форму своими данными:имя,фамилия,почтовый индекс.
f_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
f_name.send_keys("Olga")

l_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
l_name.send_keys("Leonteva")

zip_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip_code.send_keys(152909)

# Нажмите кнопку Continue.
button_continue = driver.find_element(By.CSS_SELECTOR, '#continue').click()

# Прочитайте со страницы итоговую стоимость (Total).
total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
print(total)

# Закройте браузер.
driver.quit()


# Проверьте, что итоговая сумма равна $58.29
@pytest.mark.test_03
def test_set_comparison():
    set1 = set(total)
    set2 = set("58.29")
    assert set1 == set2
