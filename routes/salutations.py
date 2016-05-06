from initializer import app

@app.route('/hello')
def hello():
    return "Hello person"

@app.route('/goodbye')
def goodbye():
    return "Goodbye person"
