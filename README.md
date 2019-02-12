# API for my company with Flask
1. Flask
2. Postgresql
3. SqlAlchemy
4. Alembic

###Postgres.

Database part:
```bash
CREATE DATABASE flask_api_trash;
CREATE USER flask with password 'flask';
GRANT ALL PRIVILEGES ON DATABASE flask_api_trash to flask;

```
####Migrations

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```