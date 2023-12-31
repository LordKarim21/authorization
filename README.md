# Authorization Project

Проект "Authorization" представляет собой веб-приложение на Django для аутентификации по номеру телефона. Пользователи могут вводить свой номер телефона и получать код авторизации, а также активировать инвайт-код для доступа к своему профилю.

## Установка и запуск

1. Склонируйте репозиторий:

```bash
git clone https://github.com/LordKarim21/authorization.git
cd authorization
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Примените миграции:

```bash
python manage.py migrate
```

4. Запустите сервер:

```bash
python manage.py runserver
```

# Сборка Docker-образа
docker build -t my-django-app .

# Запуск Docker-контейнера
docker run -p 8000:8000 my-django-app
