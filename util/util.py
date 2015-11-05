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

def getTimeNow():
    """
    获取当前日期时间戳
    :return: 时间戳
    """
    return int(time.time())