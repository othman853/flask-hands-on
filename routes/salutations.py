from initializer import app

@app.route('/hello')
@app.route('/hello/<person>')
def hello(person = 'Stranger'):
    return "Hello %s" % person

@app.route('/goodbye')
@app.route('/goodbye/<person>')
def goodbye(person = 'Stranger'):
    return "Goodbye %s" % person
