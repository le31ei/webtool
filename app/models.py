#coding=utf8

from app import db


class MailUser(db.Model):
    '''
        mailuser
    '''
    __tablename__ = "MailUser"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),index=True,unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email = email


class Users(db.Model):
    """
    普通用户model
    """
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    regDate = db.Column(db.String(50), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __init__(self, email, username, password, regDate, isActive=False, isAdmin=False):
        self.email = email
        self.username = username
        self.password = password
        self.regDate = regDate
        self.isActive = isActive
        self.isAdmin = isAdmin

    """
    flask-login必须实现的接口
    """
    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        if self.isAdmin is False:
            return False  #不能登录后台
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

class InviteCodeList(db.Model):
    """
    邀请码表
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inviteCode = db.Column(db.String(50), index=True, nullable=False, unique=True)
    codestatus = db.Column(db.Boolean, nullable=False)

    def __init__(self, inviteCode, codestatus = True):
        self.inviteCode = inviteCode
        self.codestatus = codestatus









