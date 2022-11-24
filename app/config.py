import os
from datetime import timedelta

class Config():
    DEBUG = True
    SECRET_KEY = '23_Mars_2000'
    JWT_SECRET_KEY = '23_Mars_2000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES =timedelta(days=1)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    PORT = 5000