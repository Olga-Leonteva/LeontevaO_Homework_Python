import pytest
from string_utils import StringUtils


# Принимает на вход текст, делает первую букву заглавной и возвращает этот же
# текст
# Позитивная
@pytest.mark.parametrize(
    "string, result",
    [
        ("hello", "Hello"),
           ],
)
def test_capitilize_positive(string, result):
    processor = StringUtils()
    assert processor.capitilize(string) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, result",
    [
        (None, " "),
           ],
)
def test_capitilize_negative(string, result):
    processor = StringUtils()
    assert processor.capitilize(string) == result


# Принимает на вход текст и удаляет пробелы в начале, если они есть
# Позитивная
@pytest.mark.parametrize(
    "string, result",
    [
        ("   Rik", "Rik"),
    ]
)
def test_trim_positive(string, result):
    processor = StringUtils()
    assert processor.trim(string) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, result",
    [
        (111, 111),
    ]
)
def test_trim_negative(string, result):
    processor = StringUtils()
    assert processor.trim(string) == result


# Принимает на вход текст с разделителем и возвращает список строк 1
# Позитивная
@pytest.mark.parametrize(
    "string, result",
    [
        ("а,б,в,г", ["а", "б", "в", "г"]),
            ]
)
def test_to_list_positive_1(string, result):
    processor = StringUtils()
    assert processor.to_list(string) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, result",
    [
        (None, [" "]),
            ]
)
def test_to_list_negative_1(string, result):
    processor = StringUtils()
    assert processor.to_list(string) == result


# Принимает на вход текст с разделителем и возвращает список строк 2
# Позитивная
@pytest.mark.parametrize(
    "string, delimeter, result",
    [
        ("кошка:собака:хомяк", ":", ["кошка", "собака", "хомяк"])
    ]
)
def test_to_list_positive_2(string, delimeter, result):
    processor = StringUtils()
    assert processor.to_list(string, delimeter) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, delimeter, result",
    [
        (" : : :", ":", [])
    ]
)
def test_to_list_negative_2(string, delimeter, result):
    processor = StringUtils()
    assert processor.to_list(string, delimeter) == result


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# Позитивная
@pytest.mark.parametrize('string, symbol, result',
                         [('Rik', 'k', True), ('Rik', 'w', False)])
def test_contains_positive(string, symbol, result):
    processor = StringUtils()
    assert processor.contains(string, symbol) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result',
                         [(['Rik', 'Bik'], 'k', True),
                          (['Rik', 'Bik'], 'w', False)])
def test_contains_negative(string, symbol, result):
    processor = StringUtils()
    assert processor.contains(string, symbol) == result


# Удаляет все подстроки из переданной строки
# Позитивная
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("SyPro", "k", "SyPro")
            ]
)
def test_delete_symbol_positive(string, symbol, result):
    processor = StringUtils()
    assert processor.delete_symbol(string, symbol) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        (123, 2, 13)
            ]
)
def test_delete_symbol_negative(string, symbol, result):
    processor = StringUtils()
    assert processor.delete_symbol(string, symbol) == result


# Возвращает `True`, если строка начинается с заданного символа и `False` -
# если нет
# Позитивная
@pytest.mark.parametrize('string, symbol, result',
                         [('Rik', 'R', True), ('Rik', 'w', False)])
def test_starts_with_positive(string, symbol, result):
    processor = StringUtils()
    assert processor.starts_with(string, symbol) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result',
                         [(['Rik', 'Bik'], 'R', True),
                          (['Rik', 'Bik'], 'w', False)])
def test_starts_with_negative(string, symbol, result):
    processor = StringUtils()
    assert processor.starts_with(string, symbol) == result


# Возвращает `True`, если строка заканчивается заданным символом и `False` -
# если нет
# Позитивная
@pytest.mark.parametrize('string, symbol, result',
                         [('Rik', 'k', True), ('Rik', 'w', False)])
def test_end_with_positive(string, symbol, result):
    processor = StringUtils()
    assert processor.end_with(string, symbol) == result


# Возвращает `True`, если строка пустая и `False` - если нет
@pytest.mark.parametrize('string, result',
                         [('', True), (' ', True), ('Rik', False)])
def test_is_empty_positive(string, result):
    processor = StringUtils()
    assert processor.is_empty(string) == result


# Негативная
@pytest.mark.xfail
@pytest.mark.parametrize('string, result',
                         [(1, True), ('Rik', False)])
def test_is_empty_negative(string, result):
    processor = StringUtils()
    assert processor.is_empty(string) == result


# Преобразует список элементов в строку с указанным разделителем
# Позитивная
@pytest.mark.parametrize(
    "lst, joiner, result",
    [
            ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
            (["Sky", "Pro"], ", ", "Sky, Pro"),
            (["Dog", "Rik"], "-", "Dog-Rik")
            ]
            )
def test_list_to_string_positive(lst, joiner, result):
    processor = StringUtils()
    assert processor.list_to_string(lst, joiner) == result


# Негативная
@pytest.mark.parametrize(
    "lst, joiner, result",
    [
            ((1, 2, 3, 4), ", ", "1, 2, 3, 4"),
            (("Sky", "Pro"), ", ", "Sky, Pro"),
            (("Dog", "Rik"), "-", "Dog-Rik")
            ]
            )
def test_list_to_string_negative(lst, joiner, result):
    processor = StringUtils()
    assert processor.list_to_string(lst, joiner) == result
