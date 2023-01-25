from http import HTTPStatus

from fastapi.testclient import TestClient
from tinydb import TinyDB

from fti.api.v1.views import app

db = TinyDB('default_db.json')

client = TestClient(app)


def test_get_form():
    response = client.post(
        ('/get_form/?user_email=login@domen.ru'
         '&telephone=+79599999997&username=vasya')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'form_name': 'Authentication'}


def test_get_form_without_client_data():
    response = client.post(
        ('/get_form/')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {}


def test_get_form_with_blank_value_client_data():
    response = client.post(
        ('/get_form/?username=')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'username': ''}


def test_get_form_with_additional_fields():
    response = client.post(
        ('/get_form/?user_email=login@domen.ru'
         '&telephone=+79599999997&username=vasya'
         '&home=Moscow&sex=male&register_date=21.01.1999')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'form_name': 'Registration'}

    response = client.post(
        ('/get_form/?user_email=login@domen.ru'
         '&telephone=+79599999997&username=vasya'
         '&home=Moscow&sex=male&birthday_date=21.01.1999')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'form_name': 'Authentication'}

    response = client.post(
        ('/get_form/?username=vasya'
         '&home=Moscow&sex=male&birthday_date=1999-01-21')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'form_name': 'Birthday'}


def test_get_form_with_unknown_fields():
    response = client.post(
        ('/get_form/?email=login@domen.ru'
         '&phone=+79599999997&user=vasya'
         '&home=Moscow&sex=male&date=21.01.1999')
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'email': 'email',
        'phone': 'phone',
        'user': 'text',
        'home': 'text',
        'sex': 'text',
        'date': 'date'
    }


def test_get_form_with_fail_db_structure():
    wrong_doc = db.insert({
        'name': 'Address',
        'fields': {
            'home': 'text'
        }
    })
    try:
        response = client.post(
            '/get_form/?home=Moscow&sex=male&date=21.01.1999'
        )
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        assert response.json() == {
            'detail': 'Нарушена структура документов в базе данных.'
        }
    finally:
        db.remove(doc_ids=[wrong_doc])
