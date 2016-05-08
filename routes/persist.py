from initializer import app
from models import SimpleModel
from flask import render_template

@app.route('/persist/<simple_data>')
def persist(simple_data):

    model = SimpleModel(simple_data)
    model.save(simple_data)

    last = SimpleModel.query.order_by(SimpleModel.id.desc()).first()
    
    return render_template('save_result.j2', last=last)
