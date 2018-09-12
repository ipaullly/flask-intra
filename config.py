import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xc7Qi\xfd\xf1\x8a\x9c\x0b\x06\xc6'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False