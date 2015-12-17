#coding=utf8
from app import app
from flask_mail import Message
from app.admin import mail,mycelery
from util.grabSendmail import GetVulname,get360vul
from app.models import MailUser

@mycelery.task
def send_my_email():
    with app.app_context():
        users = MailUser.query.all()
        mailto = []
        for user in users:
            mailto.append(user.email)
        mysendwoyun = GetVulname()
        resultstrwoyun = mysendwoyun.findVul()
        mysend360 = get360vul()
        result360 = mysend360.findVul()
        if resultstrwoyun or result360:
            msg = Message('每日安全简报',sender=('雷雪峰','le31ei@163.com'), recipients=mailto)
            msg.html = "<h1>每日安全简报</h1>"
            if resultstrwoyun:
                msg.html+="<h2>乌云漏洞</h2>"
                msg.html+=resultstrwoyun.encode('utf8')
            if result360:
                msg.html+="<h2>360补天漏洞</h2>"
                msg.html+=result360
            msg.html+="<h3>此邮件为自动发送，请勿回复</h3>"
            mail.send(msg)