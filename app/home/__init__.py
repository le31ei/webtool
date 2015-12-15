#coding=utf8
__author__ = 'root'
from app import app
from app.home.models import Users
from flask.ext.login import LoginManager

#初始化flask-login
login_manage = LoginManager()
login_manage.init_app(app)
login_manage.session_protection = 'strong'
login_manage.login_view='homes.login'


@login_manage.user_loader
def load_user(userid):
    '''
    flask-login模块函数回调，返回一个unicode字符
    :return:
    '''
    return Users.query.get(int(userid))