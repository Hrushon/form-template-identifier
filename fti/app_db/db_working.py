from typing import List, Union

from tinydb import TinyDB, Query
from tinydb.table import Document
from tinydb.utils import freeze

from fti.app_db.test_data import TEST_DATA
from fti.settings import DB_NAME

db: TinyDB = TinyDB(DB_NAME)


def search_documents(data) -> Union[List[Document], List]:
    """
    Функция при обращении к БД получает и возвращает все документы,
    у которых хотя бы одно поле и тип значения поля соответствует
    данным, полученным от клиента.
    """
    def test_func(document, value):
        """
        Функция сравнивает данные документов в БД с данными клиента,
        обеспечивая фильтрацию и неободимую выборку. Если в документе
        БД есть поле, отсутствующее в данных клиента, или тип
        поля не соответствует типу поля в полученных от клиента данных, то
        документ в результирующую выборку не попадает.
        """
        for key in document:
            if key not in value or value[key] != document[key]:
                return False
        return True

    return db.search(Query().fields.test(test_func, freeze(data)))


def add_test_data_db():
    """
    При выполнении данной функции происходит добавление тестовых
    данных в базу TinyDB.
    """
    db: TinyDB = TinyDB(DB_NAME)
    db.insert_multiple(TEST_DATA)


if __name__ == '__main__':
    add_test_data_db()
