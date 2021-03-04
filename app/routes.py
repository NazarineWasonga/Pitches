from flask import Flask, render_template, flash, redirect, url_for, request
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm
from flask_login import login_required, logout_user, current_user, login_user
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Nazarine'}
    pitches = [
        {
            'author': 'Nazarine Wasonga',
            'title': 'First Pitch',
            'category': 'Motivational',
            'body': 'First pitch ',
            'date_posted': 'March, 3, 2021',
            'votes': 1
        },
        {
            'author': 'Dorcas Atieno',
            'title': 'Second Pitch',
            'category': 'Learning',
            'body': 'First pitch ',
            'date_posted': 'March, 1, 2021',
            'votes': 11
        },
        {
            'author': 'Rael Akinyi',
            'title': 'Third Pitch',
            'category': 'Funny',
            'body': 'First Pitch',
            'date_posted': 'March, 2, 2021',
            'votes': 4
        }
    ]
    return render_template('index.html', pitches=pitches)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('registration.html', title='Sign Up', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    pitches = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, pitches=pitches)
