#coding=utf8

from flask import Blueprint, request, render_template, url_for

homes = Blueprint("homes", __name__, static_folder='static',  template_folder='templates')


@homes.route('/', methods = ["GET", "POST"])
@homes.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("home/index.html")