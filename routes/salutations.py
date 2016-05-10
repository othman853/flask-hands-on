from flask_login import login_required, current_user
from initializer import app
from flask import render_template

@app.route('/hello/')
@login_required
def hello(person=None):

    if person == None and current_user != None:
        person = current_user.name


    return render_template('hello.j2', person = person)
