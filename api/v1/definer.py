import re
from typing import Dict, List, Optional, Union

from fastapi import HTTPException
from tinydb.table import Document

from db_working import search_documents

ETALONS: Dict[str, str] = {
    'date': r'''
        ^((0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[012]).((1[0-9]|20)\d\d))
        |(((1[0-9]|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))$
    ''',
    'phone': r'^\+7[0-9]{10}$',
    'email': r'^.+@.+\..+$',
    'text': r'^.+$'
}


def types_definer(data: Dict[str, str]) -> Dict[str, str]:
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


def forms_definer(data: Dict[str, str]) -> Dict[str, str]:
    """
    Принимает данные от клиента в виде словаря и вызывает соответствующие
    функции для определения типов значений полей и поиска подходящей формы
    в базе данных.
    Далее сравнивает данные формы из документов в БД с данными, полученными от
    клиента, путем объединения словарей.
    В случае, если форма в базе данных отсутствует - возвращает полученный в
    качестве аргумента словарь.
    """
    data_with_types: Dict[str, str] = types_definer(data)
    forms: Union[List[Document], List] = search_documents(data_with_types)
    count_data: int = len(data_with_types)
    search_result: Optional[Document] = None

    for form in forms:
        fields: Dict[str, str] = form['fields'][0]
        count_form: int = len(fields)
        if search_result:
            if len(search_result['fields'][0]) > count_form:
                continue
        merge_dict: Dict[str, str] = {**data_with_types, **fields}
        if len(merge_dict) == count_data:
            search_result = form
            if count_form == count_data:
                break

    if search_result:
        try:
            form_name: str = search_result['form_name']
        except KeyError:
            raise HTTPException(
                status_code=500,
                detail="Нарушена структура документов в базе данных."
            )
        return {'form_name': form_name}

    return data_with_types
