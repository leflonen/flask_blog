from flask_wtf import form
from wtforms import StringField, validators
from author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.required(),
        validators.length(max=80)
        ])
