from initializer import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from models import User

LOGIN_OPERATION = 'login'
REGISTER_OPERATION = 'register'

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('login.j2', operation=REGISTER_OPERATION)

    username = request.form['name']
    password = request.form['password']

    if User.is_username_taken(username):
        flash('This username is already taken')
        return render_template('login.j2', operation=REGISTER_OPERATION)

    user = User(username, password)
    user.save()

    flash('User created successfully, you can try to log into the system now')
    return render_template('login.j2', operation=LOGIN_OPERATION)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.j2', operation=LOGIN_OPERATION)

    username = request.form['name']
    password = request.form['password']

    if username == 'name' and password == 'password':
        login_user(User(username, password))
        return render_template('deluxe_hello.j2', person=username)
    else:
        flash('Wrong username or password, try again.')
        return render_template('login.j2', operation=LOGIN_OPERATION)
