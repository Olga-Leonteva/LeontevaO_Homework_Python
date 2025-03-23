import requests
import pytest


base_url = 'https://ru.yougile.com/api-v2/'
login = 'panakushinaoa@gmail.com'
password = 'Leonteva05'
name = 'Поток_100'
company_id = 'f76a47ef-881d-4dfd-a124-857a668b03a8'


# Авторизация
def post_auth():
    data = {
        'login': login,
        'password': password,
        'companyId': company_id
    }
    resp = requests.post(base_url+'auth/keys', json=data)
    token = resp.json()["key"]
    return token


# Данные сотрудников
def get_users(token):
    resp = requests.get(base_url+'users', json=token)
    user_id = resp.json()["id"]
    return user_id


# Список проектов
def get_project(token):
    resp = requests.get(base_url+'projects', json=token)
    return resp.json()


# Создание проекта
def create_project(title, user_id=""):
    new_project = {
            "title": title,
            "users": {
                user_id: "admin"
            }
     }
    resp = requests.post(base_url + 'projects', json=new_project)
    project_id = resp.json()["id"]
    return project_id


# Поиск по id
def get_seach(project_id):
    resp = requests.get(base_url+'projects/'+project_id)
    return resp.json()


# Изменение проекта
def put_correction(new_title, user_id, project_id):
    data_cor_project = {
        'deleted': True,
        'title': new_title,
        'users': user_id
        }
    resp = requests.put(
            base_url+'projects/'+project_id, json=data_cor_project)
    return resp.json()


# Создание ногового проекта
@pytest.mark.test_post
def test_post(user_id):
    # Получить количество компаний до
    body = get_project()
    len_before = len(body)
    title = 'Rik'
    create_project(title, user_id)
    # Получить количество компаний после
    body = get_project()
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["title"] == title


@pytest.mark.test_get
def test_get(user_id):
    # Создать проект
    title = 'Кот и пес'
    new_id = create_project(title, user_id)
    # Найти по id
    project_seach = get_seach(new_id)
    assert project_seach["deleted"] is True


@pytest.mark.test_put
def test_put(user_id):
    # Создать проект
    title = 'От улыбки с танет всем теплей'
    new_id = create_project(title, user_id)
    # Изменить проект
    new_title = 'С приветом по планетам'
    project_before = put_correction(new_id, new_title, user_id)
    assert project_before['title'] == new_title
