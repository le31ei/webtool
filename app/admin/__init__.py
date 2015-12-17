#coding=utf8

from app import app
#初始化mail
from flask_mail import Mail
mail = Mail(app)


#初始化celery
from celery import Celery,platforms
mycelery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
platforms.C_FORCE_ROOT = True