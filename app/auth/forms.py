# coding: utf-8 
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo,Regexp
 
class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(),Length(1,64)], render_kw={
        "class":"form-control",
    })
    password = PasswordField("Password",validators=[DataRequired()],render_kw={
        "class":"form-control",
    })
    remember_me = BooleanField("Keep me Logged in",render_kw={
        "class":"custom-control-input" ,
        "id":"login"
    })
    submit = SubmitField("Log In",render_kw={
        "class":"btn btn-primary px-5"
    })