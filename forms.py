from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from models import Kayttaja

class LoginForm(FlaskForm):
    name = StringField('Käyttäjänimi', validators=[DataRequired()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    submit = SubmitField('Kirjaudu sisään')

class RegistrationForm(FlaskForm):
    name = StringField('Käyttäjänimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Length(min=6), DataRequired(), Email()])
    password = PasswordField('Salasana', validators=[DataRequired(), 
                                                    Length(min=6, message='Salasanan on oltava vähintään kuusi merkkiä pitkä.')])
    password2 = PasswordField(
        'Salasana uudelleen', validators=[DataRequired(), EqualTo('password', message='Salasana ei täsmää.')])
    submit = SubmitField('Rekisteröidy')

    #def validate_username(self, name):
      #  user = Kayttaja.query.filter_by(nimi=name.data).first()
    #    if user is not None:
     #       raise ValidationError('Käyttäjänimi on jo varattu.')

    def validate_email(self, email):
        user = Kayttaja.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Käytäthän toista sähköpostiosoitetta.')