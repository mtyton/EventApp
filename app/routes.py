from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import EventAddForm, LoginForm, RegisterForm
from app.models import Event, User
from flask_login import current_user, login_user, logout_user, login_required

import datetime


@app.route('/index')
@login_required
def base_view():
    events = Event.query.all()
    return render_template('index.html', events=events)



@app.route('/index/<int:pk>')
@login_required
def detail_view(pk):
    event = Event.query.filter_by(id=1).first()
    return render_template('detail.html', event=event)



@app.route('/add', methods=('POST', 'GET'))
@login_required
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
            flash('Something went wrong')
            return redirect(url_for('login'))
    else:
        return render_template('add.html', form=form)


@app.route("/register", methods=("POST", "GET"))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('base_view'))
    else:
        form = RegisterForm()
        if request.method == "POST":
            if form.validate_on_submit:
                username = form.username.data
                password = form.password.data
                confirm = form.confirm_password.data
                email = form.email.data
                if password == confirm:
                    user = User()
                    user.username = username
                    user.email = email
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('base_view'))
                else:
                    return render_template('register.html', form=form, message="passwords don't match")
            else:
                return render_template('register.html', form=form, message="something is wrong with your form")
        else:
            return render_template('register.html', form=form, message="Fill the form please")


@app.route("/login", methods=("POST", "GET"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base_view'))
    else:
        form = LoginForm()
        if request.method == "POST":

            if form.validate_on_submit:
                user = User.query.filter_by(username=form.username.data).first()
                if user is None or not user.check_password(form.password.data):
                    flash("INvalid username or password")
                    return redirect(url_for("login"))
                login_user(user)
                return redirect(url_for("base_view"))
            else:
                return render_template("login.html", form=form)

        return render_template("login.html", form=form)



@app.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('base_view'))


