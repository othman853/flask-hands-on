from initializer import app
from flask import render_template

@app.route('/hello')
@app.route('/hello/<person>')
def hello(person = 'Stranger'):
    return "Hello %s" % person

@app.route('/goodbye')
@app.route('/goodbye/<person>')
def goodbye(person = 'Stranger'):
    return "Goodbye %s" % person

@app.route('/colorful/hello')
def colorful_hello(person = 'Stranger'):
    return render_template('colorful_hello.j2', person=person)
