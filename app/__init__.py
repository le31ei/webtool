#coding=utf8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = app.config['SECRET_KEY']


from admin.views import admins
from home.views import homes

app.register_blueprint(admins)
app.register_blueprint(homes)


#migrate
from app.admin import models
from app.home import models

