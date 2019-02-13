from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from trash.app import app, db
from trash import models


migrate = Migrate(app, db, directory="trash/migrations")
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
