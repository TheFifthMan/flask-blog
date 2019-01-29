# coding: utf-8 
'''
需要安装：
    1. flask-sqlalchemy
    2. flask-mail
    3. python-dotenv
'''
# app初始化
# 新建初始化文件,使用工厂函数来创建 app 以便后续写unittest的时候，能够动态的传入不同的配置，从而生成 app 实例
# app/__init__.py
from flask import Flask 
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_mail  import Mail
 
# 数据库连接
db = SQLAlchemy()
# 发送邮件
mail = Mail()
 
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 初始化各种插件
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)

    # 声明蓝图
    from app.index import index as index_bp
    app.register_blueprint(index_bp)

    from app.admin import admin as admin_bp
    app.register_blueprint(admin_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)


    if not app.debug:
        # 记录到文件
        if not os.path.exists('logs'):
                    os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/flasky.log',maxBytes=10240,backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('app start.')

    return app