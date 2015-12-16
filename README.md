webtool
=======

使用说明：<br>
    根目录添加config.py，格式：<br>
    #coding=utf8<br>
    #调试<br>
    DEBUG = True<br>
    #后台路径<br>
    ADMIN_PATH = 'xxx'<br>
    #数据库<br>
    SQLALCHEMY_DATABASE_URI = "mysql://xxx:xxx@localhost/webtool"<br>
    SQLALCHEMY_TRACK_MODIFICATIONS = True<br>
    #session 密钥<br>
    SECRET_KEY = 'xxx'<br>


###V0.1:
    登录功能

###v0.1.1:
    后台登录功能以及后台index页面布局
    
###v0.1.2:
    添加celery后台异步任务，自动抓取乌云、360、漏洞盒子最新漏洞

###v0.1.3
    前台注册、登录及邀请码的完成