from sqlalchemy import Column, String, Integer
from initializer import database

class SimpleModel(database.Model):

    __tablename__= 'simple_models'
    id = Column(Integer, primary_key=True)
    value = Column(String)

    def __init__(self, value):
        self.value = value

    def save(self):
        database.session.add(self)
        database.session.commit()
        return self
