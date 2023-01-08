"""
При выполнении данного модуля происодит добавление тестовых
данных в базу TinyDB.
"""
from typing import Dict, List, Union

from tinydb import TinyDB

from settings import DB_NAME

db: TinyDB = TinyDB(DB_NAME)

test_data: List[Dict[str, Union[str, List[Dict[str, str]]]]] = [
    {
        'form_name': 'Birthday',
        'fields': [{
            'username': 'text',
            'birthday_date': 'date'
        }]
    },
    {
        'form_name': 'Authentication',
        'fields': [{
            'username': 'text',
            'user_email': 'email',
            'telephone': 'phone'
        }]
    },
    {
        'form_name': 'Follow_list',
        'fields': [{
            'username': 'text'
        }]
    },
    {
        'form_name': 'Calendar',
        'fields': [{
            'choice_date': 'date'
        }]
    },
    {
        'form_name': 'Change_email',
        'fields': [{
            'user_email': 'email'
        }]
    },
    {
        'form_name': 'Registration',
        'fields': [{
            'username': 'text',
            'user_email': 'email',
            'register_date': 'date',
            'telephone': 'phone'
        }]
    }
]

if __name__ == '__main__':
    db.insert_multiple(test_data)
