Метод PageObject и Allure

Проект состоит из трех частей:
1) Тестирование Калькулятора
2) Тестирование Формы ввода данных
3) Тестирование работы алгоритма по совершению покупок в олнлайн магазине

Страницы описывающие методы для работы с функционалом сайтов и странницы тестов находятся в соответсвующих папках:
1) calculator:
    * config.py, 
    * Data_calc.py, 
    * Result_calc.py
    * calc_page_object_test.py
2) form:
    * FormPage.py
    * form_page_object_test.py
3) shop:
    * CartPage.py, 
    * ShopPage.py, 
    * ShopResultPage.py, 
    * SwagLabsPage.py, 
    * YourInformationPage.py
    * Shop_page_object_test.py

Тестирование платформ выполняется в файлах:
- calc_page_object_test.py
- form_page_object_test.py
- Shop_page_object_test.py

Чтобы запустить тестирование необходимо открыть новый терминал и выполнить команду "python -m pytest --alluredir allure-result".

Результаты теста сохранятся в папку "allure-result".

Для генерирования отчета в терминал вводится команда "allure serve allure-results". Отчет откроется в окне вашего браузера.
