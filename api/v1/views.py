from fastapi import FastAPI, Request

from api.v1.definer import forms_definer

app = FastAPI()


@app.post('/get_form/')
def get_form(request: Request):
    """
    В соответствии с условиями ТЗ получает данные от клиента из QueryParams
    вида '?value1=2022-01-20&value2=login@rambler.ru&value3=+795655366874'.
    Из данных создает словарь, и вызывает функцию definer c этим
    словарем в качестве аргументов.
    Через 'request.query_params' не получилось реализовать,
    так как при создании словаря из QueryParams под капотом FastAPI
    пропадает знак '+' в номере телефона.
    """
    data = str(request.url).split('/get_form/?')
    if len(data) == 1:
        return dict()
    data = data[1].split('&')
    data_list = [item.split('=') for item in data]
    data_dict = {k: v for k, v in data_list}
    return forms_definer(data_dict)
