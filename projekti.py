import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('mysql+pymysql://Admin:admin1@localhost/musahaku')
#db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://Admin:admin1@localhost/musahaku'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)


@app.route("/")
def main():
    #kayttajat = db.execute("SELECT nimi FROM kayttaja").fetchall()
    kayttajat = Kayttaja.query.all()
    return render_template("index.html", result=kayttajat)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    name = name.capitalize()
    return render_template("hello.html", name=name)

@app.route("/money", methods=["POST"])
def money():
    amount = request.form.get("amount")
    return render_template("money.html", amount=amount)

if __name__ == "__main__":
    main()