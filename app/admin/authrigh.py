#coding=utf8
from functools import wraps
from flask import session,redirect, url_for
from util.util import getTimeNow
from flask.ext.login import current_user,logout_user
from .models import AdminUser


def isLogin(func):
    """
    判断是否是后台用户的装饰器
    fix：修复前后台互相登录的问题
    :return:
    """
    @wraps(func)
    def isUserlogin(*args, **kwargs):
        if not current_user.is_authenticated():
            logout_user()
            return redirect(url_for('homes.logout'))
        return func(*args, **kwargs)
    return isUserlogin


def isLoginTimeOut(func):
    """
    判断session是否超时的装饰器
    超过10分钟，则退出登录
    :param func:
    :return:
    """
    @wraps(func)
    def isTimeOut(*args, **kwargs):
        if session.get('user') is not None:
            user = session.get('user')
            if getTimeNow() - user['loginTime'] > 600:
                return redirect(url_for('admins.logout'))
        return func(*args,**kwargs)
    return isTimeOut
