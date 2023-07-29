import os
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False