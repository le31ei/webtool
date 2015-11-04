from flask import Blueprint,render_template
from app import app

admins = Blueprint("admins", __name__, static_folder='static', template_folder='templates',url_prefix='/'+app.config['ADMIN_PATH'])

@admins.route('/')
@admins.route('/login')
def login():
    return render_template('admins/login.html')