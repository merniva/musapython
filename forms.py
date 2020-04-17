from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from models import Kayttaja

class LoginForm(FlaskForm):
    name = StringField('Käyttäjänimi', validators=[DataRequired()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    submit = SubmitField('Kirjaudu')

class RegistrationForm(FlaskForm):
    name = StringField('Käyttäjänimi', validators=[DataRequired(message='Käyttäjänimi on pakollinen tieto.')])
    email = StringField('Sähköposti', validators=[DataRequired(message='Sähköpostiosoite on pakollinen tieto.'), Email(message='Virheellinen sähköpostiosoite.')])
    password = PasswordField('Salasana', validators=[DataRequired(message='Salasana on pakollinen tieto.'), 
                                                    Length(min=6, max=100, message='Salasanan on oltava vähintään kuusi merkkiä pitkä.')])
    password2 = PasswordField(
        'Salasana uudelleen', validators=[DataRequired(message='Toistathan salasanan.'), EqualTo('password', message='Salasana ei täsmää.')])
    submit = SubmitField('Rekisteröidy')

    #def validate_username(self, name):
      #  user = Kayttaja.query.filter_by(nimi=name.data).first()
    #    if user is not None:
     #       raise ValidationError('Käyttäjänimi on jo varattu.')

    def validate_email(self, email):
        user = Kayttaja.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Käytäthän toista sähköpostiosoitetta.')