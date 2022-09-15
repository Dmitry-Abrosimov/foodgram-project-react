# Foodgram
![foodgram workflow](https://github.com/Dmitry-Abrosimov/foodgram-project-react/actions/workflows/foodgram-project-react.yml/badge.svg)

Сервер http://158.160.9.114/

## Технологии:

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### Описание:
На сайте foodgram пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Зависимости
```
asgiref==3.2.10
Django==3.1.14
django-filter==2.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.8.0
gunicorn==20.0.4
psycopg2-binary==2.9
PyJWT==2.1.0
pytz==2020.1
sqlparse==0.3.1
```

### Установка
1. **Клонируйте репозиторий:**
```sh
git clone https://github.com/Dmitry-Abrosimov/foodgram-project-react.git
```

2. **Создайте файл .env с переменными окружения для работы с базой данных:**
```sh
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

3. **Перейдите в папку с файлом docker-compose.yaml и запустите контейнеры:**
```sh
docker-compose up -d --build
```
4. **Выполните миграции в контейнере web:**
```sh
docker-compose exec backend python manage.py migrate
```
5. **Создайте суперпользователя:**
```sh
docker-compose exec backend python manage.py createsuperuser
```
6. **Соберите статику:**
```sh
docker-compose exec backend python manage.py collectstatic --no-input
```
7. **Заполните базу данных:**
```sh
docker-compose exec backend python manage.py loaddata db.json 
```
8. **Для остановки контейнеров воспользуйтесь командой:**
```sh
docker-compose down -v
```
