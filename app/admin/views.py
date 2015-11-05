#coding=utf8
from flask import Blueprint,render_template,redirect,url_for,\
    request,jsonify,session
from app import app
from models import AdminUser
from util.util import getPasswordMd5,getTimeNow
from authrigh import isLogin

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
        session.pop('user', None)
        return render_template('admins/login.html')
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']
        if username != "" and password != "":
            user = AdminUser.query.filter_by(uname=username).first()
            if user != None:
                if user.passwd == getPasswordMd5(password,user.regDate):
                    session['user'] = {'username': username, 'loginTime': getTimeNow()}
                    return jsonify({'url': url_for('admins.index'), 'msg': 'success'})
    return jsonify({'msg': 'failed'})


@admins.route('/index', methods=['GET', 'POST'])
@isLogin
#@isLoginTimeOut
def index():
    """
    后台首页视图
    :return:
    """
    if request.method == "GET":
        return render_template('admins/index/pages/index.html')
    if request.method == "POST":
        return "123"

@admins.route('/logout', methods = ['GET', 'POST'])
def logout():
    """
    退出函数 v0.1
    :return: 跳转的url
    """
    session.pop('user',None)
    return redirect(url_for("admins.login"))


