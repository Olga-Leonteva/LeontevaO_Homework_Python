import allure
from Kinopoisk_API import Kinopoisk_API
import pytest


@allure.epic("API tests")
@allure.feature("Позитивные проверки")
@allure.title("Поиск по названию фильма")
@pytest.mark.test_01_api
def test_seach_film_by_title():
    api = Kinopoisk_API()
    new_title = "The Beekeeper"
    response = api.seach_film_by_title(new_title)
    assert response.status_code == 200, "Баг"
    assert response.json()["docs"][0]["alternativeName"] == new_title


@allure.title("Поиск по имени актера")
@pytest.mark.test_02_api
def test_seach_name_person():
    api = Kinopoisk_API()
    name_person = "Johnny Depp"
    response = api.seach_name_person(name_person)
    assert response.json()["docs"][0]["enName"] == name_person
    assert response.status_code == 200, "Баг"


@allure.title("Поиск фильма по id актера")
@pytest.mark.test_03_api
def test_seach_film_person_id():
    api = Kinopoisk_API()
    person_id = 6245
    response = api.seach_film_person_id(person_id)
    print(response)
    assert response.json()["docs"][0]["id"] == 6461896
    assert response.status_code == 200, "Баг"


@allure.feature("Негативные проверки")
@allure.title("Поиск по неверному id")
@pytest.mark.test_04_api
def test_seach_wrong_id():
    api = Kinopoisk_API()
    wrong_id = "249"
    response = api.seach_wrong_id(wrong_id)
    assert response.status_code == 400, "Баг"
    assert response.json()["error"] == "Bad Request"


@allure.title("Поиск несуществующего жанра")
@pytest.mark.test_05_api
def test_seach_wrong_category():
    api = Kinopoisk_API()
    wrong_category = "небылица"
    response = api.seach_wrong_category(wrong_category)
    assert response.status_code == 200, "Баг"
    assert response.json()["total"] == 0
