#coding=utf8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from admin.views import admins
from home.views import homes

app.register_blueprint(admins)
app.register_blueprint(homes)
