from flask.ext.login import UserMixin

class User(UserMixin):

    def __init__(self, name, password):
        self.id = 0
        self.name = name
        self.password = password
