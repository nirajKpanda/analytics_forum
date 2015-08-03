from flask import Flask, Blueprint
from blog.forum.view import forum
from blog.helpers.ext import db


def create_app(Config):
    app = Flask(__name__)
    app.config.from_object("blog.configs.default.DevelopmentConfig")
    app.config.from_object(Config)

    register_blueprints(app)
    configure_extensions(app)

    return app

def register_blueprints(app):
    app.register_blueprint(forum, url_prefix="/forum")


def configure_extensions(app):
    db.init_app(app)


