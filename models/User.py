from flask.ext.login import UserMixin
from initializer import database
from sqlalchemy import Column, Integer, String

class User(database.Model, UserMixin):

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)

    def __init__(self, name, password):
        self.id = 0
        self.name = name
        self.password = password

    def save(self):
        database.session.add(self)
        database.session.commit()
        return self
