"""
Задание 2
В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(), принимающую в качестве аргумента
код валюты (например, USD, EUR, SGD, ...) и возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.

Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте:

есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

"""

import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[(element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_rate/amendment
    result_value = currency_dict.get(code.upper())  ## здесь должно оказаться результирующее значение float
    return result_value


print(currency_rates("USD"))
print(currency_rates("AUD"))
print(currency_rates("eur"))
print(currency_rates("BYN"))
print(currency_rates("noname"))