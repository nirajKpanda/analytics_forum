from flask.ext.script import Manager, Server
from blog.app import create_app
from blog.helpers.ext import db
from blog.models import *

from blog.configs.default import DevelopmentConfig as Config 

app = create_app(Config)
manager = Manager(app)
manager.add_command("runserver", Server())


@manager.command
def run():
    app.run(host="0.0.0.0", debug=True)


@manager.command
def createdb():
    db.create_all()

if __name__ == "__main__":
    manager.run()

