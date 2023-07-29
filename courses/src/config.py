from datetime import datetime


class Config(object):
    SQLALCHEMY_DATABASE_URI = ("postgresql://postgres:admin@35.188.80.59:5432/postgres")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = 3600