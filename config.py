import os
from flask import Flask, render_template, request, flash, session, redirect, url_for

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://Admin:admin1@localhost/musahaku'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = SECRET_KEY