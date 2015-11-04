#coding=utf8
from functools import wraps
from flask import session,redirect, url_for

def isLogin(func):
    """
    判断是否登录的装饰器
    :return:
    """
    @wraps(func)
    def isUserlogin(*args, **kwargs):
        if session.get('user') == None:
            return redirect(url_for('admins.logout'))
        return func(*args, **kwargs)
    return isUserlogin