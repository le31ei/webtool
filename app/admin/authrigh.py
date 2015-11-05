#coding=utf8
from functools import wraps
from flask import session,redirect, url_for
from util.util import getTimeNow

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

def isLoginTimeOut(func):
    """
    判断session是否超时的装饰器
    超过10分钟，则退出登录
    :param func:
    :return:
    """
    @wraps(func)
    def isTimeOut(*args, **kwargs):
        if session.get('user') != None:
            user = session.get('user')
            if getTimeNow() - user['loginTime'] > 600:
                return redirect(url_for('admins.logout'))
        return func(*args,**kwargs)
    return isTimeOut
