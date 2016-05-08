from sqlalchemy import Column, String, Integer
from initializer import database

class SimpleModel(database.Model):

    __tablename__= 'simple_model'
    id = Column(Integer, primary_key=True)
    value = Column(String)

    def __init__(self, value):
        self.value = value

    def save(self, data):
        database.session.add(SimpleModel(data))
        database.session.commit()
        return self
