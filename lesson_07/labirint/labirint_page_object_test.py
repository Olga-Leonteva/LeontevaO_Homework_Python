from selenium import webdriver
import pytest
from pages.MainPage import MainPage


@pytest.mark.test_labirint_page
def test_card_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("Python")
