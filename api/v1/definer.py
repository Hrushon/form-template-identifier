import re

from db import search_form

ETALONS = {
    'date': r'''
        ^((0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[012]).((1[0-9]|20)\d\d))
        |(((1[0-9]|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))$
    ''',
    'phone': r'^\+7[0-9]{10}$',
    'email': r'^.+@.+\..+$',
    'text': r'^.+$'
}


def types_definer(data):
    """
    Определяет тип данных полей переданных клиентом, сравнивая значения с
    регулярными выражениями, по итогу возвращает словарь с названием поля
    и типом данных этого поля.
    """
    for name, val in data.items():
        for name_type, etalon in ETALONS.items():
            if re.match(etalon, val, re.X):
                data[name] = name_type
                break
    return data


def forms_definer(data):
    """
    Принимает данные от клиента в виде словаря и вызывает соответствующие
    функции для определения типов значений полей и поиска подходящей формы
    в базе данных.
    """
    data_with_types = types_definer(data)
    return search_form(data_with_types)
