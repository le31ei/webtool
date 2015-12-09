#coding=utf8

from flask import Blueprint, request, render_template
from util.util import create_validate_code
import StringIO
from app import app

homes = Blueprint("homes", __name__, static_folder='static',  template_folder='templates')


@homes.route('/', methods = ["GET", "POST"])
@homes.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("home/login.html")



@homes.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("home/register.html")


@homes.route('/forgetpass', methods = ["GET", "POST"])
def forgetpass():
    if request.method == "GET":
        return render_template("home/forgetpass.html")

@homes.route('/randomcode/<rand>', methods = ["GET"])
def randomcode(rand):
    if request.method == "GET":
        code_img,strs = create_validate_code()
        buf = StringIO.StringIO()
        code_img.save(buf,'JPEG',quality=70)

        buf_str = buf.getvalue()
        response = app.make_response(buf_str)
        response.headers['Content-Type'] = 'image/jpeg'
        return response