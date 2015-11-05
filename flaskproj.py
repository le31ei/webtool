#coding=utf8
from app import app
from flask import session
from datetime import timedelta

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
    #设置session过期时间
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)
