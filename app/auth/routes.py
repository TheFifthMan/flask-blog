from . import auth
from .views import Login

auth.add_url_rule('/login',view_func=Login.as_view('login'))
