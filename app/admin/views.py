#coding=utf8
from flask import Blueprint,render_template,redirect,url_for,\
    request,jsonify,session
from app import app
from models import AdminUser, MailUser
from util.util import getPasswordMd5, getServerInfo
from flask.ext.login import login_user, login_required, logout_user
from celerysend import send_my_email
from app import db

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
        logout_user()
        return render_template('admins/login.html')
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']
        if username != "" and password != "":
            user = AdminUser.query.filter_by(uname=username).first()
            if user != None:
                if user.passwd == getPasswordMd5(password,user.regDate):
                    login_user(user)
                    session.permanent = True  #session有效时间
                    return jsonify({'url': url_for('admins.index'), 'msg': 'success'})
    return jsonify({'msg': 'failed'})


@admins.route('/index', methods=['GET', 'POST'])
@login_required
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
@login_required
def logout():
    """
    退出函数 v0.1
    :return: 跳转的url
    """
    logout_user()
    return redirect(url_for("admins.login"))


@admins.route('/getServerInfo', methods=['GET'])
@login_required
def serverinfo():
    cpuinfo = getServerInfo.getCPUuse()
    meminfo = getServerInfo.getMemuse()
    return jsonify({'cpu':cpuinfo,'mem':meminfo})


@admins.route('/usercontrol/<action>', methods=["GET","POST"])
@login_required
def usercontrol(action):
    if request.method=="GET":
        if action == 'listuser':
            return render_template("admins/index/pages/userlist.html")


@admins.route('/sendmail/<action>', methods=["GET", "POST"])
@login_required
def sendmail(action):
    '''
    定时抓取乌云等网站的信息，并通过邮件发送
    :return:
    '''
    if request.method == "POST":
        username = request.json['adduser']
        usermail = request.json['usermail']
        if username != "" and usermail != "":
            useraddmail = MailUser(username,usermail)
            if useraddmail != None:
                try:
                    db.session.add(useraddmail)
                    db.session.commit()
                    return jsonify({'msg':'success'})
                except Exception, e:
                    print e
        return jsonify({'msg':'faild'})
    if action == "index":
        return render_template('admins/index/pages/sendmail/maillist.html')
    elif action == "send":
        send_my_email.delay()
        return jsonify({"send":"ok"})
    elif action == 'adduser':
        return render_template('admins/index/pages/sendmail/addmailuser.html')
