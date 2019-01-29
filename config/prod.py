from .general import Config
import os 

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or "mysql+pymysql://root:qwe123@127.0.0.1/blog"
 