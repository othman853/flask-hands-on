from flask import Flask
from flask import render_template
from flask_login import LoginManager
from models import User

app = Flask(__name__)

app.secret_key = 'flask_hands_on_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

login_manager = LoginManager(app)
login_manager.login_view = 'get_login'

@login_manager.user_loader
def login_user_loader(user_id):
    return User('name', 'password')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.j2'), 404

from routes.login import *
from routes.salutations import *
from routes.deluxe_salutations import *
