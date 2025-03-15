from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def click_checout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
