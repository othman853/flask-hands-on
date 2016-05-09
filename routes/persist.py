from initializer import app
from models import SimpleModel
from flask import render_template

@app.route('/persist/<simple_data>')
def persist(simple_data):

    model = SimpleModel(simple_data)
    model.save()

    last = model.query.order_by(model.id.desc()).first()

    return render_template('save_result.j2', last=last)
