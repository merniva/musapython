from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from projekti import login

db = SQLAlchemy()

class Kayttaja(UserMixin, db.Model):
    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    salasana = db.Column(db.String, nullable=False)
    def set_password(self, password):
        self.salasana = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        #print("Password is " + self.salasana + " " + password)
        #return self.salasana == password
        return check_password_hash(self.salasana, password)

    def __repr__(self):
        return '<User {}>'.format(self.nimi)
#class User(UserMixin, db.Model):
    # ...
    

#@login.user_loader
#def load_user(id):
#    return Kayttaja.query.get(int(id))