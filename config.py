import os
 
class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #google plus settings
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    SCOPE = os.environ["SCOPE"]
    GOOGLE_TOKEN_URI = os.environ["GOOGLE_TOKEN_URI"]
    GOOGLE_AUTH_URI = os.environ["GOOGLE_AUTH_URI"]
    GOOGLE_REVOKE_URI = os.environ["GOOGLE_REVOKE_URI"]


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = False
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # print SQLALCHEMY_DATABASE_URI


class ProductionConfig(BaseConfig):
    DEBUG = False