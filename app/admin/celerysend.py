#coding=utf8
from app import app
from flask_mail import Message
from app.admin import mail,mycelery
from util.grabSendmail import GetVulname
from app.admin.models import MailUser
from app import db
from app.admin.models import MailUser

@mycelery.task
def send_my_email():
    with app.app_context():
        users = MailUser.query.all()
        mailto = []
        for user in users:
            mailto.append(user.email)
        mysend = GetVulname()
        resultstr = mysend.findVul()
        if resultstr:
            msg = Message('每日安全简报',sender=('雷雪峰','le31ei@163.com'), recipients=mailto)
            msg.html="<h1>乌云漏洞</h1>"
            msg.html+=resultstr.encode('utf8')+"<h3>此邮件为自动发送，请勿回复</h3>"
            mail.send(msg)