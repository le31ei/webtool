#coding=utf8

from app import db


class AdminUser(db.Model):
    """
    管理员model
    """
    __tablename__ = 'AdminUser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(150), unique=True, nullable=False, index=True)
    passwd = db.Column(db.String(150), nullable=False)
    regDate = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100))

    def __init__(self,username,password,regDate,email='null'):
        self.uname = username
        self.passwd = password
        self.regDate = regDate
        self.email = email

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


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









