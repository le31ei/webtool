#coding=utf8
from flask import Blueprint,render_template,redirect,url_for,\
    request
from app import app

admins = Blueprint("admins", __name__, static_folder='static', template_folder='templates',url_prefix='/'+app.config['ADMIN_PATH'])

@admins.route('/',methods = ['GET','POST'])
@admins.route('/login', methods=['GET', 'POST'])
def login():
    """
        登录函数 v0.1
        升级：限制登录次数
    :return:
    """
    if request.method == "GET":
        return render_template('admins/login.html')

@admins.route('/logout', methods = ['GET', 'POST'])
def logout():
    return redirect(url_for("admins.login"))


