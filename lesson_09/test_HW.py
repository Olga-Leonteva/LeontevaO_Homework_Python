from sqlalchemy import create_engine, inspect, text
import pytest

db_connection_string = 'postgresql://postgres:123456789@localhost:5432/QA'
db = create_engine(db_connection_string)


@pytest.mark.test_0_connect
def test_db_connect():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[2] == 'subject'


@pytest.mark.test_0_select
def test_select():
    connection = db.connect()     # Создаем соединение
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()   # Получаем результат в виде словарей
    row1 = rows[0]

    assert row1['subject_id'] == 1

    connection.close()      # Закрываем соединение


# Тест добавление
@pytest.mark.test_01_insert
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_title, :new_id)")
    connection.execute(sql, {"new_title": "Technology", "new_id": 16})

    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()   # Получаем результат в виде словарей
    count = len(rows)
    assert count == 16
    transaction.rollback()  # всегда откатываем изменения после теста
    connection.close()


# Тест изменение
@pytest.mark.test_02_update
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_title, :new_id)")
    connection.execute(sql, {"new_title": "Technology", "new_id": 16})

    res = connection.execute(text(
        "SELECT * FROM subject WHERE subject_id = :id"), {"id": 16})

    sql = text(
        "UPDATE subject SET subject_title = :title WHERE subject_id = :id")
    connection.execute(sql, {"title": 'Astronomy', "id": '16'})

    res_new = connection.execute(text(
        "SELECT * FROM subject WHERE subject_id = :id"), {"id": 16})

    assert res != res_new
    transaction.rollback()  # всегда откатываем изменения после теста
    connection.close()


# Тест удаление
@pytest.mark.test_03_delete
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_title, :new_id)")
    connection.execute(sql, {"new_title": "Technology", "new_id": 16})

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 16})

    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()   # Получаем результат в виде словарей
    count = len(rows)
    assert count == 15
    transaction.rollback()  # всегда откатываем изменения после теста
    connection.close()
