from selenium import webdriver


driver = webdriver.Chrome()

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'}

driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie)

cookies = driver.get_cookies()  # переменная, в которую соберутся cookies
print(cookies)  # запрос на вывод данных в терминал

driver.refresh()

driver.quit()
