from flask_login import login_required, current_user
from initializer import app
from flask import render_template

@app.route('/deluxe/hello/<person>')
@app.route('/deluxe/hello/')
@login_required
def deluxe_hello(person=None):

    if person == None and current_user != None:
        person = current_user.name


    return render_template('deluxe_hello.j2', person = person)
