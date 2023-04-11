import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')