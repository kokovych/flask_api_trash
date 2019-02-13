from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask:flask@localhost/flask_api_trash'
    return app

app = create_app()
db = SQLAlchemy(app)


if __name__ == '__main__':

    @app.route('/')
    def hello():
        return "Hello World!"

    app.run()
