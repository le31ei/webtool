#coding=utf8
from app import app
from flask.ext.login import LoginManager
from .models import AdminUser

#初始化flask-login
login_manage = LoginManager()
login_manage.init_app(app)
login_manage.session_protection = 'strong'
login_manage.login_view='admins.login'


@login_manage.user_loader
def load_user(userid):
    '''
    flask-login模块函数回调，返回一个unicode字符
    :return:
    '''
    return AdminUser.query.get(int(userid))