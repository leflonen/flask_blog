from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    fullname = StringField('Full name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        validators.length(min=4, max=25)
        ])
    password = PasswordField('New Password',[
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(min=4, max=60)
        ])
    confirm = PasswordField('Repeat password')

class LoginForm(Form):
    username = StringField('Username',[
        validators.Required(),
        validators.length(min=4,max=25),
        ])
    password = PasswordField('Password',[
        validators.Required(),
        validators.Length(min=4, max=60)
        ])
