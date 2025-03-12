from selenium import webdriver
import pytest
from shop.ShopPage import ShopPage
from shop.SwagLabsPage import SwagLabsPage
from shop.YourInformationPage import YourInformationPage
from shop.CartPage import CartPage
from shop.ShopResultPage import ShopResultPage


@pytest.mark.test_shop_page
def test_shop():
    browser = webdriver.Chrome()
    swag_labs = SwagLabsPage(browser)
    swag_labs.autoauthorization("standard_user", "secret_sauce")
    shop = ShopPage(browser)
    shop.add_products()
    cart_page = CartPage(browser)
    cart_page.get()
    cart_page.click_checout()
    your_information_page = YourInformationPage(browser)
    your_information_page.your_information("Olga", "Leonteva", "152909")
    your_information_page.click_continue()
    result_shop = ShopResultPage(browser)
    total = result_shop.shop_result()
    assert total == "Total: $58.29"
