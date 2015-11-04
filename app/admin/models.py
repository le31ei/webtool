#coding=utf8

from app import db


class AdminUser(db.Model):

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

