from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import EventAddForm, LoginForm
from app.models import Event, User
from flask_login import current_user, login_user, logout_user

import datetime


@app.route('/index')
def base_view():
    events = Event.query.all()
    return render_template('index.html', events=events)


@app.route('/index/<int:pk>')
def detail_view(pk):
    event = Event.query.filter_by(id=1).first()
    return render_template('detail.html', event=event)


@app.route('/add', methods=('POST', 'GET'))
def add():
    form = EventAddForm()
    if request.method == "POST":
        if form.validate_on_submit():

            event = Event(name=form.name.data, date=form.date.data)
            db.session.add(event)
            db.session.commit()
            flash('Congratulations, you have added an event!')
            return redirect(url_for('base_view'))
        else:
            flash('Somethign went wrong')
            return redirect(url_for('base_view'))

    else:

        return render_template('add.html', form=form)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.user.is_authenticated():
        pass


@app.route("/login", methods=("POST", "GET"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base_view'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user=User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash("INvalid username or password")
                return redirect(url_for("login"))
            login_user(user)
            return redirect(url_for("base_view"))

        return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


