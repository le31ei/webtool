#coding=utf8

from flask import Blueprint

homes = Blueprint("homes", __name__, static_folder='static',  template_folder='templates')