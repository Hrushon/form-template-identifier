from typing import Dict, List, Union

from fastapi import FastAPI, Request

from api.v1.definer import forms_definer

app: FastAPI = FastAPI()


@app.post('/get_form/')
def get_form(request: Request) -> Union[Dict[str, str], Dict]:
    """
    В соответствии с условиями ТЗ получает данные от клиента из QueryParams
    вида '?value1=2022-01-20&value2=login@rambler.ru&value3=+795655366874'.
    Из данных создает словарь, и вызывает функцию "forms_definer" c этим
    словарем в качестве аргументов.
    Через 'request.query_params' не получилось реализовать,
    так как при создании словаря из QueryParams под капотом FastAPI
    пропадает знак '+' в номере телефона.
    """
    data: List[str] = str(request.url).split('/get_form/?')
    if len(data) == 1:
        return dict()

    data = data[1].split('&')
    data_list: List[List[str]] = [item.split('=') for item in data]
    data_dict: Dict[str, str] = {k: v for k, v in data_list}
    return forms_definer(data_dict)
