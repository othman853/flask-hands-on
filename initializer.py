from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.j2'), 404

from routes.salutations import *
