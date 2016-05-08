from initializer import app
from models import SimpleModel
from flask import render_template

@app.route('/list')
def list_records():
    records = SimpleModel.query.all()

    return render_template('list.j2', records=records)
