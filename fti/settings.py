"""
Модуль с настройками и константами приложения.
"""
import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv()

DB_NAME: str = os.getenv('DB_NAME', default='default_db.json')

REGEX_PATERNS: Dict[str, str] = {
    'date': r'''
        ^((0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[012]).((1[0-9]|20)\d\d))
        |(((1[0-9]|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))$
    ''',
    'phone': r'^\+7[0-9]{10}$',
    'email': r'^.+@.+\..+$',
    'text': r'^.+$'
}
