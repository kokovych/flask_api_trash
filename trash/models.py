from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PersonalAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
