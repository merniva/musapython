from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Käyttäjänimi', validators=[DataRequired()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    remember_me = BooleanField('Muista minut')
    submit = SubmitField('Kirjaudu sisään')