from initializer import app
from flask import render_template, request, redirect, url_for
from flask_login import login_user
from models.User import User

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.j2')


@app.route('/login', methods=['POST'])
def post_login():

    username = request.form['name']
    password = request.form['password']

    if username == 'name' and password == 'password':
        login_user(User(username, password))
        return render_template('deluxe_hello.j2', person=username)
    else:
        return render_template('forbidden.j2')
