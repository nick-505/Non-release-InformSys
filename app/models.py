from app import db
from flask_login import UserMixin
""" from app import login
 """
### USER MODEL ###
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(65), index=True, unique=True)
    password = db.Column(db.String(128))

    def get_id(self):
        return (self.id)

### EMPLOYEE MODEL ###


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    subject = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)

    def get_id(self):
        return (self.id)




