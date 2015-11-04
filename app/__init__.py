#coding=utf8
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from admin.views import admins
from home.views import homes

app.register_blueprint(admins)
app.register_blueprint(homes)
