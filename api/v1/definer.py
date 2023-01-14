import re
from http import HTTPStatus
from typing import Dict, List, Optional, Union

from fastapi import HTTPException
from tinydb.table import Document

from app_db.db_working import search_documents
from settings import REGEX_PATERNS


def types_definer(data: Dict[str, str]) -> Dict[str, str]:
    """
    Определяет тип данных полей переданных клиентом, сравнивая значения с
    регулярными выражениями, по итогу возвращает словарь с названием поля
    и типом данных этого поля.
    """
    for name, val in data.items():
        for name_type, etalon in REGEX_PATERNS.items():
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
    Если найдена соответствующая форма в базе данных - возвращает название
    найденной формы, в противном случае - возвращает форму, созданную на
    основе полученных от клиента данных.
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
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail='Нарушена структура документов в базе данных.'
            )
        return {'form_name': form_name}

    return data_with_types
