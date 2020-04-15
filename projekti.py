import os

from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *
from forms import LoginForm, RegistrationForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('mysql+pymysql://Admin:admin1@localhost/musahaku')
#db = scoped_session(sessionmaker(bind=engine))
SECRET_KEY = os.urandom(32)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://Admin:admin1@localhost/musahaku'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
db.init_app(app)
login = LoginManager(app)

@login.user_loader
def load_user(id):
    if id is not None:
        return Kayttaja.query.get(int(id))
    return None

@login.unauthorized_handler
def unauthorized():
    flash('Kirjaudu sisään nähdäksesi sivun.')
    return redirect(url_for('login'))


@app.route('/', methods=('GET', 'POST'))
def main():
    #kayttajat = db.execute("SELECT nimi FROM kayttaja").fetchall()
    #kayttajat = Kayttaja.query.all()
    return render_template("index.html") #, result=kayttajat

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=['GET', 'POST'])
@login_required
def hello():
    name = request.form.get("name")
    name = name.capitalize()
    return render_template("hello.html", name=name)

@app.route("/money", methods=["POST"])
def money():
    amount = request.form.get("amount")
    return render_template("money.html", amount=amount)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Kayttaja.query.filter_by(nimi=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Virheellinen käyttäjänimi tai salasana!')
            return render_template('index.html')
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('main'))
    return render_template('login.html', title='Kirjaudu sisään', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = Kayttaja.query.filter_by(nimi=form.name.data).first()  # Check if user exists
        if existing_user is None:
            user = Kayttaja(nimi=form.name.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Rekisteröityminen onnistui!')
            return redirect(url_for('login'))
        flash('Käyttäjänimi on jo varattu.')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)

if __name__ == "__main__":
    main()