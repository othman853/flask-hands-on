from initializer import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, login_required, logout_user
from models import User

LOGIN_OPERATION = 'login'
REGISTER_OPERATION = 'register'
SALUTATION = 'hello'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')

    return _redirect(LOGIN_OPERATION)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        flash('To register a new user you must logout first. Do it by hitting /logout')
        return _redirect(SALUTATION)

    if request.method == 'GET':
        return render_template('login.j2', operation=REGISTER_OPERATION)

    username, password = _from_form(request.form)

    if User.is_username_taken(username):
        flash('This username is already taken')
        return _redirect(REGISTER_OPERATION)

    user = User(username, password)
    user.save()

    flash('User created successfully, you can try to log into the system now')
    return _redirect(LOGIN_OPERATION)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return _redirect(SALUTATION)

    if request.method == 'GET':
        return render_template('login.j2', operation=LOGIN_OPERATION)

    username, password = _from_form(request.form)

    user = User.find_by_username(username)

    if user == None or user.password != password:
        flash('Wrong username or password, try again.')
        return _redirect(LOGIN_OPERATION)

    login_user(user)
    return _redirect(SALUTATION)

def _from_form(request_form):
    return request_form['name'], request_form['password']

def _redirect(operation):
    return redirect(url_for(operation))
