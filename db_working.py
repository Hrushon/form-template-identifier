from typing import List, Union

from tinydb import TinyDB, Query
from tinydb.table import Document

from settings import DB_NAME
from test_data import TEST_DATA

db: TinyDB = TinyDB(DB_NAME)


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


def add_test_data_db():
    """
    При выполнении данной функции происходит добавление тестовых
    данных в базу TinyDB.
    """
    db: TinyDB = TinyDB(DB_NAME)
    db.insert_multiple(TEST_DATA)


if __name__ == '__main__':
    add_test_data_db()
