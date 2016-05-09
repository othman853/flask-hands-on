from flask.ext.login import UserMixin
from initializer import database
from sqlalchemy import Column, Integer, String

class User(database.Model, UserMixin):
    __tablename__='users'

    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String, unique=True)
    password = Column(String)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        database.session.add(self)
        database.session.commit()
        return self

    @staticmethod
    def is_username_taken(username):
        return User.find_by_username(username) != None

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(name=username).one_or_none()
