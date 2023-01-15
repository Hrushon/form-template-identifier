from typing import Dict, List, Union

TEST_DATA: List[Dict[str, Union[str, List[Dict[str, str]]]]] = [
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
