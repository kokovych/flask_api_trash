from flask import Flask
from models import db


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask:flask@localhost/flask_api_trash'

db.init_app(app)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
