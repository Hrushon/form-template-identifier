![Workflow](https://github.com/Hrushon/form-template-identifier/actions/workflows/identifier_workflow.yml/badge.svg)

![Python](https://img.shields.io/badge/Python-3.8.9-blue?style=for-the-badge&logo=python&logoColor=yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0-blueviolet?style=for-the-badge&logo=fastapi&logoColor=green)
![TinyDB](https://img.shields.io/badge/TinyDB-4.7.0-red?style=for-the-badge&logo=tinydb&logoColor=blue)

# Form Template Identifier
## Приложение для определения заполненных форм

Приложение позволяет определить название формы, хранящейся в собственной базе данных, соответствующей данным, поступившим от пользователя. При отсутствии подходящей формы в базе данных динамически создает и возвращает форму с названием и типом полей, соответствующими данным пользователя.

## Порядок установки проекта

Клонируем репозиторий и переходим в директорию с приложением:
```
git clone https://github.com/Hrushon/form-template-identifier.git
```
```
cd ./form-template-identifier/
```

## Порядок запуска проекта:

### Первый вариант (с тестированием)

Cоздаем и активируем виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Устанавливаем зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Добавляем тестовые документы в базу данных:
```
python -m fti.app_db.db_working
```
Тестируем проект:
```
pytest -v
```
Создаем и открываем для редактирования файл .env:
```
nano .env
```
#### Структура env-файла:
```
# указываем имя Вашей базы данных (например: 'forms_db.json')
DB_NAME='forms_db.json'
```
Запускаем проект:
```
python -m fti.main
```

### Второй вариант (Docker)
Создаем и открываем для редактирования файл .env:
```
nano .env
```
#### Структура env-файла:
```
# указываем имя Вашей базы данных (например: 'forms_db.json')
DB_NAME='forms_db.json'
```
Создаем образ:
```
sudo docker build -t fti .
```
Запускаем контейнер из образа:
```
sudo docker run --name fti -it -p 8000:8000 fti
```

### Структура базы данных:

Пример структуры базы данных:
```
TEST_DATA: List[Dict[str, Union[str, List[Dict[str, str]]]]] = [
    {
        'form_name': 'Birthday',
        'fields': {
            'username': 'text',
            'birthday_date': 'date'
        }
    },
    {
        ...
    }
]
```

## Эндпоинты приложения

### Определение формы
```
/get_form/     метод: POST
```
