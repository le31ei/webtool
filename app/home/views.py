#coding=utf8

from flask import Blueprint, request, render_template,session,\
    jsonify, url_for, redirect
from util.util import create_validate_code
import StringIO
from app import app, db
from util.util import getPasswordMd5, getTimeNow, isEmailString
from .models import Users, InviteCodeList
from flask.ext.login import login_required, login_user, logout_user

homes = Blueprint("homes", __name__, static_folder='static',  template_folder='templates')


@homes.route("/index", methods = ["GET", "POST"])
@login_required
def index():
    return render_template("home/index/pages/index.html")


@homes.route('/', methods = ["GET", "POST"])
@homes.route('/login', methods= ["GET", "POST"])
def login():
    """
    用户登录视图
    :return:
    """
    if request.method == "GET":
        return render_template("home/login.html")
    elif request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]
        yzCode = request.json["yzCode"]
        try:
            session_yzCode = session["yzCode"]
            if getPasswordMd5(yzCode, "O(@(#@EJW@!JIEW") != session_yzCode:
                session.pop("yzCode", None)
                return jsonify({"status":"yzcode", "msg":"验证码错误"})
        except:
            return jsonify({"status":"yzcode", "msg":"验证码错误"})
        if isEmailString(username): #email形式登录
            users = Users.query.filter_by(email=username).first()
        else:
            users = Users.query.filter_by(username=username).first()

        if users != None:
            password_md5 = getPasswordMd5(password,users.regDate)
            if password_md5 == users.password:#登录成功
                login_user(users)
                session.permanent = True
                return jsonify({"status":"success","url":url_for("homes.index")})

        return jsonify({"status":"failed", "msg":"用户名或密码错误"})


@homes.route("/logout", methods = ["GET"])
def logout():
    logout_user()
    return redirect(url_for("homes.login"))




@homes.route('/register', methods = ["GET", "POST"])
def register():
    """
    用户注册视图
    :return:
    """
    if request.method == "GET":
        return render_template("home/register.html")
    elif request.method == "POST":
        inviteCode = request.json['invitecode']
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        if not isEmailString(email):
            return jsonify({"stauts":"failed", "msg":"请输入正确的邮箱"})
        regDate = getTimeNow()
        try:
            invicode = InviteCodeList.query.filter_by(inviteCode=inviteCode).first()
            if invicode.codestatus == True:
                try:
                    users = Users(email, username, getPasswordMd5(password,str(regDate)), regDate)
                    db.session.add(users)
                    db.session.commit()
                    #邀请码失效
                    #invicode.codestatus = False
                    #db.session.commit()
                    return jsonify({"status":"success", "url": url_for("homes.login")})
                except:
                    return jsonify({"status":"failed", "msg":"填写的信息有误"})
            else:
                return jsonify({"status":"failed", "msg":"邀请码已被使用"})
        except:
            return jsonify({"status":"failed", "msg":"邀请码有误"})




@homes.route('/forgetpass', methods = ["GET", "POST"])
def forgetpass():
    """
    用户忘记密码视图
    :return:
    """
    if request.method == "GET":
        return render_template("home/forgetpass.html")

@homes.route('/randomcode/<rand>', methods = ["GET"])
def randomcode(rand):
    """
    验证码视图
    :param rand:
    :return:
    """
    if request.method == "GET":
        code_img, strs = create_validate_code() #验证码
        session['yzCode'] = getPasswordMd5(strs, "O(@(#@EJW@!JIEW")
        buf = StringIO.StringIO()
        code_img.save(buf,'JPEG',quality=70)
        buf_str = buf.getvalue()
        response = app.make_response(buf_str)
        response.headers['Content-Type'] = 'image/jpeg'
        return response