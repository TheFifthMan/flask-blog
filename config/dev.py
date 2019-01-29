from .general import Config
import os 

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_SQLALCHEMY_DATABASE_URI") or "mysql+pymysql://root:qwe123@127.0.0.1/blog"