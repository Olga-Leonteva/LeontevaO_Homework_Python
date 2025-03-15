from selenium.webdriver.common.by import By


class ShopResultPage:
    def __init__(self, browser):
        self.driver = browser

    def shop_result(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
        return total
