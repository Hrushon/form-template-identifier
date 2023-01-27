import re
from http import HTTPStatus
from typing import Dict, List, Optional, Union

from fastapi import HTTPException
from tinydb.table import Document

from fti.app_db.db_working import search_documents
from fti.settings import REGEX_PATTERNS


def types_definer(data: Dict[str, str]) -> Dict[str, str]:
    """
    Определяет тип данных полей переданных клиентом, сравнивая значения с
    регулярными выражениями, по итогу возвращает словарь с названием поля
    и типом данных этого поля.
    Как по мне, множественные ветви сравнения выглядят не очень красиво,
    да и такой подход вставляет палки в колеса будущей масштабируемости,
    но придумать что-то лучше и производительнее я не смог.
    Вложенный цикл медленнее и не по-питонячи, а 'itertools.product'
    еще медленнее вложенного цикла.
    """
    for name, value in data.items():
        if re.match(REGEX_PATTERNS['date'], value, re.X):
            data[name] = 'date'
        elif re.match(REGEX_PATTERNS['phone'], value, re.X):
            data[name] = 'phone'
        elif re.match(REGEX_PATTERNS['email'], value, re.X):
            data[name] = 'email'
        elif re.match(REGEX_PATTERNS['text'], value, re.X):
            data[name] = 'text'

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
        fields: Dict[str, str] = form['fields']
        count_form: int = len(fields)
        if search_result:
            if len(search_result['fields']) > count_form:
                continue
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
