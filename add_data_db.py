from tinydb import TinyDB

db = TinyDB('forms_db.json')

test_data = [
    {
        'form_name': 'Birthday',
        'fields': {
            'username': 'text',
            'birthday_date': 'date'
        }
    },
    {
        'form_name': 'Authentication',
        'fields': {
            'username': 'text',
            'user_email': 'email',
            'telephone': 'phone'
        }
    },
    {
        'form_name': 'Follow_list',
        'fields': {
            'username': 'text'
        }
    },
    {
        'form_name': 'Calendar',
        'fields': {
            'choice_date': 'date'
        }
    },
    {
        'form_name': 'Change_email',
        'fields': {
            'user_email': 'email'
        }
    },
    {
        'form_name': 'Registration',
        'fields': {
            'username': 'text',
            'user_email': 'email',
            'register_date': 'date',
            'telephone': 'phone'
        }
    }
]

db.insert_multiple(test_data)
