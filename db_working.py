from typing import List, Union

from tinydb import TinyDB, Query
from tinydb.table import Document

db: TinyDB = TinyDB('forms_db.json')


def search_documents(data) -> Union[List[Document], List]:
    """
    Придумать поисковый запрос к Tiny, чтобы удовлетворить требования ТЗ, не
    получилось. Поэтому функция при обращении к БД получает и возвращает все
    документы, у которых хотя бы одно поле и тип значения поля соответствует
    данным, полученным от клиента.
    Поисковый запрос создается на "лету".
    """
    count_data: int = len(data)
    query_string: str = str()
    cnt: int = 0
    for key, value in data.items():
        query_string += f'(Query().fields.any(Query()["{key}"] == "{value}"))'
        cnt += 1
        if cnt != count_data:
            query_string += ' | '

    return db.search(eval(query_string))
