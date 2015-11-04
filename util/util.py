#coding=utf8
import hashlib

def getPasswordMd5(password, regDate):
    """
    获取MD5值 v0.1
    :param password: 用户密码
    :param regDate: 注册日期（盐）
    :return: MD5
    """
    return 0