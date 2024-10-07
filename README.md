# Проект "Виджет банковских операций"
## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.  Проект, 
который на бэкенде будет готовить данные для отображения в новом виджете.
* Реализована функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера.
* Реализована функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера.
* Реализована функция, которая принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки
* Реализована функция, которая принимает на вход строку с датой в формате 
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024").
* Реализована функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
* Реализована функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
* Реализована функция, которая принимает на вход список словарей, представляющих транзакции.
        Функция возвращает итератор, который поочередно выдает транзакции,
        где валюта операции соответствует заданной (например, USD).
* Реализован генератор, который принимает список словарей с транзакциями 
 и возвращает описание каждой операции по очереди.
* Реализован генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров.
* Реализован декоратор, автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
## Установка:

1. Клонируйте репозиторий:
```
https://github.com/skarlainn/homeworks1.git
```
2. Установите зависимости:
```
poetry install
```
## Тестирование
* Добавлены тесты модуля masks 
* Добавлены тесты модуля widget
* Добавлены тесты модуля processing
* Добавлены тесты модуля generators
* Добавлены тесты модуля decorators

feature/homework_12_1

feature/homework_11_1
## Используемые функции:
1. Функция скрывающая номер карты и счета.
2. Функция сортировки по дате.
3. Функция фильтрации в операциях по счетам.
4. Функция выдающая транзакции, где валюта операции соответствует заданной.
5. Функция возвращающая описание каждой операции по очереди.
6. Функция генерирующая номера карт в заданном диапазоне.
7. Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. 
feature/homework_12_2
8. Добавлено логгирование для файлов masks и utils.


develop
## Тестирование:
Для запуска тестирования необходимо в терминале ввести "pytest"

## Документация:

Покрытие тестами 100%
develop

## Использование:
## Документация:
## Лицензия: