#coding=utf8
import hashlib
import time,base64

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


def getRamdomString(str):
    """
    生成一个唯一的字符串用于激活码及注册功能,以及用户的userid
    str: 用户名
    :return:
    """
    m = hashlib.md5()
    m.update(str(time.time())+ str)
    return base64.encodestring(m.digest())[:-3].replace('/', '$').encode('utf-8')