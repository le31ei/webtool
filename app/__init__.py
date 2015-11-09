#coding=utf8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = app.config['SECRET_KEY']

#初始化flask-login
login_manage = LoginManager()
login_manage.init_app(app)
login_manage.session_protection = 'strong'


from admin.views import admins
from home.views import homes

app.register_blueprint(admins)
app.register_blueprint(homes)
