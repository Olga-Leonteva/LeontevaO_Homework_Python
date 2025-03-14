from selenium import webdriver
import pytest
from Data_calc import Data_calc
from Result_calc import Result_calc


@pytest.mark.test_calc_page
def test_calc():
    browser = webdriver.Chrome()
    data_calc = Data_calc(browser)
    data_calc.timer()
    data_calc.cluck_button_calc()
    result_calc = Result_calc(browser)
    result_calc.click_equals()
    result_calc.result_calculator()
    sum = result_calc.get_result()
    assert sum == 15
    result_calc.close_driver()
