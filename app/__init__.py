#coding=utf8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import session


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = app.config['SECRET_KEY']


from app.models import Users
#flask-login初始化
login_manage = LoginManager()
login_manage.init_app(app)
login_manage.session_protection = 'strong'
login_manage.login_view = 'homes.login'


@login_manage.user_loader
def load_user_admin(userid):
    '''
    flask-login模块函数回调，返回一个unicode字符
    :return:
    '''
    return Users.query.get(int(userid))


#注册蓝图需在最后
from admin.views import admins
from home.views import homes

app.register_blueprint(admins)
app.register_blueprint(homes)


#migrate
from app import models


