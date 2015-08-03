import os


class DevelopmentConfig(object):
    _basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(32)
    SESSION_TIMEOUT = 600 # ten minutes
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_basedir, 'blogger.sqlite')
    SQLALCHEMY_ECHO = False

