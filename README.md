# Блогикум - платформа для публикации постов (часть 2)

Проект является продолжением разработки сайта Блогикум. 

## Функции проекта

* Доступны: лента записей с публикациями пользователей, страницы с информацией 
о проекте и правилами платформы. Также можно открыть отдельную страницу с 
постом, страницу определённой категории, на которой будут доступны посты 
выбранной категории.
* Подключена база данных.
* Есть доступ к админ-панели.
* Отсутствует возможность регистрации пользователей и создания новых постов 
через интерфейс сайта. Это можно сделать только через админ-панель.

## Стек технологий
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/)
* [HTML](https://developer.mozilla.org/ru/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/ru/docs/Web/CSS)
* [Bootstrap](https://getbootstrap.com/)

## Как развернуть проект
1. Клонируйте репозиторий и перейдите в директорию django_sprint3
```bash
git clone git@github.com:igorKolomitseff/django_sprint3.git
cd django_sprint3
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux и macOS
source venv/Scripts/activate  # Для Windows
```

3. Обновите pip и установите зависимости проекта:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейдите в директорию blogicum и примените миграции:
```bash
cd blogicum/
python3 manage.py migrate
```

5. Загрузите подготовленные данные (фикстуру) в базу данных:
```bash
python3 manage.py loaddata db.json 
```

6. Создайте суперпользователя, укажите запрашиваемые данные:
```bash
python3 manage.py createsuperuser
```

7. Запустите проект:
```bash
python3 manage.py runserver
```

Откройте браузер и перейдите по адресу 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) для доступа главной странице 
проекта и [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) для 
доступа к административной панели

### Автор

[Игорь Коломыцев](https://github.com/igorKolomitseff)
