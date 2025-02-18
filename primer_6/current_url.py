from selenium import webdriver

browser = webdriver.Chrome()


browser.get("https://chlist.sitechco.ru/")
url = browser.current_url
print(url)

browser.quit()
