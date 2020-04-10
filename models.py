from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Kayttaja(db.Model):
    __tablename__ = "kayttaja"
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    salasana = db.Column(db.String, nullable=False)
    trn_date = db.Column(db.DateTime, nullable=False)
