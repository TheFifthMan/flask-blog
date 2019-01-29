from flask.views import MethodView
from flask import render_template
from .forms import LoginForm

class Login(MethodView):
    def __init__(self,**kw):
        super(Login,self).__init__(**kw)
        self.form = LoginForm()
 
    def get(self):
        return render_template("auth/login.html",form=self.form)
    
    def post(self):
        if self.form.validate_on_submit():
            email = self.form.email.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.verify_password(self.form.password.data):
                login_user(user)
                flash("Login Succeed!")
                next = request.args.get("next")
                if next is None or not next.startwith("/"):
                    next = url_for('admin.index')
                return redirect(next)
        flash("invlida username or password")
        return render_template("auth/login.html",form=self.form)