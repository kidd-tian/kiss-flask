#-*- conding: utf-8 -*-

from os.path import dirname, abspath

CUR_DIR = dirname(abspath(__file__))

DEBUG = True

CSRF_ENABLED = True

CSRF_SESSION_KEY = 'ac6676f03b1c723f64fac44d8642cb58'

SECRET_KEY = 'b456d6c9cc3d7d38ca971da0b1d932f0'

#DB
SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:123456@localhost/test'