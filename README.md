webtool
=======
web工具平台
-------

使用说明：<br>
    根目录添加config.py，格式：<br>
    ```python
    \#coding=utf8<br>
    \#调试<br>
    DEBUG = True<br>
    \#后台路径<br>
    ADMIN_PATH = 'xxx'<br>
    \#数据库<br>
    SQLALCHEMY_DATABASE_URI = "mysql://xxx:xxx@localhost/webtool"<br>
    SQLALCHEMY_TRACK_MODIFICATIONS = True<br>
    \#session 密钥<br>
    SECRET_KEY = 'xxx'<br>


#V0.1:
    登录功能<br>

#v0.1.1:
    后台登录功能以及后台index页面布局<br>