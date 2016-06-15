import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '29=+m68(x%1g0y=h3z8ef+m-zv7qf^3x%h$&ao#xkzds^4=6jq'


class ProductionSettings(Settings):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'sindec-api',
        'host': os.environ.get('MONGODB_URI')
    }
    SECRET_KEY = os.environ.get('SECRET_KEY')


class StagingSettings(Settings):
    DEVELOPMENT = True
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'sindec-api',
        'host': os.environ.get('MONGODB_URI')
    }
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentSettings(Settings):
    DEVELOPMENT = True
    DEBUG = True


class TestingSettings(Settings):
    TESTING = True