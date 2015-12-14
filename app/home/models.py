#coding=utf-8

from app import db

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

    def __init__(self, email, username, password, regDate, isActive=False):
        self.email = email
        self.username = username
        self.password = password
        self.regDate = regDate
        self.isActive = isActive

    """
    flask-login必须实现的接口
    """
    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
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
