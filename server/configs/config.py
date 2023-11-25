from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    """Set Flask configuration from .env file."""

    # General Config
    DEBUG = True
    TESTING = False
    SECRET_KEY = getenv("SECRET_KEY", None)
    FLASK_ENV = getenv("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
