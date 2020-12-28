from os import environ
from dotenv import load_dotenv
load_dotenv()

class Base:
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    SECRET_KEY = ''
    MAIL_SERVER  = environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    # MAIL_USE_TLS = bool(environ.get('MAIL_USE_TLS'))
    # MAIL_DEBUG  = bool(environ.get('MAIL_DEBUG'))
    MAIL_USE_TLS = True
    MAIL_DEBUG  = True
    TESTING = False
    MAIL_SUPPRESS_SEND = False
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER  = environ.get('MAIL_USERNAME')