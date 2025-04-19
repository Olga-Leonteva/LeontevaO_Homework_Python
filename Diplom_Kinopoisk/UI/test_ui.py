from Kinopoisk_UI import Kinopoisk_UI
import pytest


@pytest.mark.test_01_ui
def test_home_page():
    ui = Kinopoisk_UI()
    title = ui.title_home_page()
    assert title == ('Кинопоиск'), 'Баг'


@pytest.mark.test_02_ui
def test_quick_search():
    ui = Kinopoisk_UI()
    film = ui.quick_search()
    assert film == ("Мастер и Маргарита"), 'Баг'


@pytest.mark.test_03_ui
def test_button_login():
    ui = Kinopoisk_UI()
    ui.button_login()
    button_login = ui.number()
    assert button_login == ("Введите номер телефона"), 'Баг'


@pytest.mark.test_04_ui
def test_film_free():
    ui = Kinopoisk_UI
    ui.film_reee()
    page_l = ui.page_login()
    assert page_l == ("Введите номер телефона")


@pytest.mark.test_05_ui
def test_random_seach():
    ui = Kinopoisk_UI
    ui.button_magnifying_glass()
    ui.quick_search()
