#coding=utf8
import hashlib
import time

def getPasswordMd5(password, regDate):
    """
    获取MD5值 v0.1
    :param password: 用户密码
    :param regDate: 注册日期（盐）
    :return: MD5
    """
    m = hashlib.md5()
    m.update(password+regDate)
    return m.hexdigest()

def getRegTime():
    """
    获取注册日期
    :return: 注册时间戳
    """
    return int(time.time())