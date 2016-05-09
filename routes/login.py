from initializer import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from models import User

LOGIN_OPERATION = 'login'
REGISTER_OPERATION = 'register'

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return _render(REGISTER_OPERATION)

    username, password = _from_form(request.form)

    if User.is_username_taken(username):
        flash('This username is already taken')
        return _render(REGISTER_OPERATION)

    user = User(username, password)
    user.save()

    flash('User created successfully, you can try to log into the system now')
    return _render(LOGIN_OPERATION)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.j2', operation=LOGIN_OPERATION)

    username, password = _from_form(request.form)

    user = User.find_by_username(username)

    if user == None or user.password != password:
        flash('Wrong username or password, try again.')
        return _render(LOGIN_OPERATION)

    login_user(user)
    return render_template('deluxe_hello.j2', person=user.name)

def _from_form(request_form):
    return request_form['name'], request_form['password']

def _render(operation):
    return render_template('login.j2', operation=operation)
