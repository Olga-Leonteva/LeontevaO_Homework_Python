from selenium import webdriver
import pytest
from FormPage import FormPage


@pytest.mark.test_form_page
def test_form():
    browser = webdriver.Chrome()
    form_page = FormPage(browser)
    form_page.data()
    form_page.click_button()
    form_page.t_color()
    form_page.close_driver()
