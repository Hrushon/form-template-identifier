from tinydb import TinyDB

db = TinyDB('forms_db.json')


def search_form(data):
    """
    Производит нехитрый поиск по имеющимся формам в базе данных и в случае
    успеха возвращает название подходящей формы.
    В случае, если форма в базе данных отсутствует - возвращает полученный в
    качестве аргумента словарь.
    Придумать поисковый запрос к Tiny, чтобы удовлетворить требования ТЗ не
    получилось, хоть и прочитал документацию. Поэтому функция при каждом
    обращении трясет с БД все имеющиеся документы.
    """
    forms = db.all()
    count_data = len(data)
    search_result = None

    for form in forms:
        fields = form['fields']
        count_form = len(fields)
        if search_result:
            if len(search_result['fields']) > count_form:
                continue
        merge_dict = {**data, **fields}
        if len(merge_dict) == count_data:
            search_result = form
            if count_form == count_data:
                break

    if not search_result:
        return data
    return {'form_name': search_result['form_name']}
