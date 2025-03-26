import requests
import pytest


base_url = 'https://ru.yougile.com/api-v2/'
login = 'panakushinaoa@gmail.com'
password = 'Leonteva05'
name = 'Поток_100'
company_id = 'f76a47ef-881d-4dfd-a124-857a668b03a8'
user_id = '02cc163e-f39f-4a1a-ac03-c0f2a351459e'
my_headers = {
    "Authorization": "Bearer ZqvBRDfnK9mco8yl0HGmXXKoNuABieBD5TkG960HoJhOPJnAIJdLIZnOv920klnr"
    }


# Авторизация
# def post_auth():
#     data = {
#         'login': login,
#         'password': password,
#         'companyId': company_id
#     }
#     resp = requests.post(base_url+'auth/keys', json=data)
#     token = resp.json()["key"]
#     return token


# Данные сотрудников
# def get_users(token):
# resp = requests.get(base_url+'users', json=token)
# user_id = resp.json()["id"]
# return user_id


# Список проектов
def get_project_count():
    resp = requests.get(base_url+'projects', headers=my_headers)
    return resp.json()["paging"]["count"]


# Создание проекта
def create_project(title, user_id):
    new_project = {
            "title": title,
            "users": {
                user_id: "admin"
            }
     }
    resp = requests.post(
        base_url + 'projects', json=new_project, headers=my_headers)
    project_id = resp.json()["id"]
    return project_id


# Поиск по id
def get_seach(project_id):
    resp = requests.get(base_url+'projects/'+project_id, headers=my_headers)
    return resp.json()


def get_seach_no_token(project_id):
    resp = requests.get(base_url+'projects/'+project_id)
    return resp


# Изменение проекта
def put_correction(new_title, user_id, project_id):
    data_cor_project = {
        'title': new_title,
        'users': {
                user_id: "admin"
            }
        }
    resp = requests.put(
            base_url+'projects/'+project_id, json=data_cor_project, headers=my_headers)
    return resp


# Создание ногового проекта
@pytest.mark.test_01_post
def test_post():
    # Получить количество компаний до
    len_before = get_project_count()
    title = 'Rik'
    project_id = create_project(title, user_id)
    # Получить количество компаний после
    len_after = get_project_count()
    assert len_after - len_before == 1
    assert get_seach(project_id)['title'] == title


@pytest.mark.test_02_get
def test_get():
    # Создать проект
    title = 'Кот и пес'
    new_id = create_project(title, user_id)
    # Найти по id
    project_seach = get_seach(new_id)
    assert project_seach["title"] == title
    assert project_seach["id"] == new_id


@pytest.mark.test_03_put
def test_put():
    # Создать проект
    title = 'От улыбки с танет всем теплей'
    new_id = create_project(title, user_id)
    # Изменить проект
    new_title = 'С приветом по планетам'
    put_correction(new_title, user_id, new_id)
    assert get_seach(new_id)['title'] == new_title


# Негативные тесты:
# Изменение с несушествующего проекта
def test_put_neg():
    new_id = '99999'
    # Изменить проект
    new_title = 'С приветом по планетам'
    resp = put_correction(new_title, user_id, new_id)
    assert resp.status_code == 404


# Поиск несуществующего id
def test_get_neg():
    resp = get_seach_no_token('999999')
    assert resp.status_code == 401


# Создание с пустым заголовком
def test_post_neg():
    new_project = {
            "title": "",
            "users": {
                user_id: "admin"
            }
     }
    resp = requests.post(
        base_url + 'projects', json=new_project, headers=my_headers)
    assert resp.status_code == 400
