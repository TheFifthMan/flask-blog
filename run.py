# coding: utf-8 
'''
需要安装 
    1.flask-migrate
'''

from app import create_app,db
from flask_migrate import Migrate
app = create_app("default")
migrate = Migrate(app, db)


@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def deploy():
    pass