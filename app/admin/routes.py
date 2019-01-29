from . import admin 

admin.add_url_rule('/index',view_func=Index.as_view('index'))
