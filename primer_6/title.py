from selenium import webdriver

browser = webdriver.Chrome()


browser.get("https://chlist.sitechco.ru/")
current_title = browser.title
print(current_title)

browser.quit()
