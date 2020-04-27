from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import *
from forms import LoginForm, RegistrationForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required


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
    return render_template("etusivu.html")

@app.route("/artistihaku", methods=['GET', 'POST'])
def artistihaku():
    return render_template("artistihaku.html")

@app.route("/kayttajahaku", methods=['GET', 'POST'])
@login_required
def kayttajahaku():
    return render_template("kayttajahaku.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Kayttaja.query.filter_by(nimi=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Virheellinen käyttäjänimi tai salasana!')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('kayttajahaku'))
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
        existing_user = Kayttaja.query.filter_by(nimi=form.name.data).first()
        if existing_user is None:
            user = Kayttaja(nimi=form.name.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Rekisteröityminen onnistui!')
            return redirect(url_for('login'))
        flash('Käyttäjänimi on jo varattu.')
        return redirect(url_for('register'))
    return render_template('register.html', title='Rekisteröidy', form=form)

if __name__ == "__main__":
    main()