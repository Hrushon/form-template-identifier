![Python](https://img.shields.io/badge/Python-3.8.9-blue?style=for-the-badge&logo=python&logoColor=yellow)
![TinyDB](https://img.shields.io/badge/TinyDB-4.7.0-red?style=for-the-badge&logo=tinydb&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0-blueviolet?style=for-the-badge&logo=fastapi&logoColor=yellow)

# FORM TENPLATE IDENTIFIER
## Приложение для определения заполненных форм

Приложение позволяет определить название формы, хранящейся в собственной базе данных, соответствующей данным поступившим от пользователя. При отсутствии подходящей формы в базе данных динамически создает и возвращает форму с названием и типом полей данных пользователя.

## Порядок установки проекта

Клонируем репозиторий и переходим в директорию с приложением:
```
git clone https://github.com/Hrushon/form-template-identifier.git
```
```
cd ./form-template-identifier/
```
## Структура env-файла:

Создаем и открываем для редактирования файл .env:
```
sudo nano .env
```
В файл вносим следующие данные:
```
# указываем имя базы данных
DB_NAME=forms_db.json
```
## Порядок запуска проекта:

Cоздаем и активируем виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установливаем зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Создаем и добавляем тестовые документы в базу данных:
```
python manage.py migrate
```
Запускаем проект:
```
python main.py
```

## Эндпоинты приложения

### Определение формы
```
/get_form/     метод: POST
```
