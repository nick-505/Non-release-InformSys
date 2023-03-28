from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash,  check_password_hash
from app import app

db = SQLAlchemy()

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


# Models for many to many relationships
subStud = db.Table('subStud',
                   db.Column('subject_id', db.ForeignKey('subject.id')),
                   db.Column('student_id', db.ForeignKey('student.id')))

subEmp = db.Table('subEmp',
                  db.Column('employee_id', db.ForeignKey('employee.id')),
                  db.Column('subject_id', db.ForeignKey('subject.id')),
                  db.Column('student_id', db.ForeignKey('student.id')))


### USER MODEL ###
class User(UserMixin, db.Model):
    # Данные для авторизации
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), index=True, unique=True)
    password = db.Column(db.String(128))

    # Информация о репетиторе
    personal_info_id = db.Column(db.Integer, db.ForeignKey('employee.id'))


    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def get_id(self):
        return (self.id)

    def get_username(self):
        return (self.username)
    

### EMPLOYEE MODEL ###
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.Text)
    subjects = db.relationship('Subject', secondary=subEmp, backref=db.backref('employees'))
    phone = db.Column(db.Text)
    email = db.Column(db.Text)

    def get_id(self):
        return (self.id)
    
### SUBJECT MODEL ###
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.Text)

### STUDENT MODEL ###
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.Text)
    subjects = db.relationship('Subject', secondary=subStud, backref=db.backref('students'))
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    

### LESSONS MODEL ###
class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    price = db.Column(db.Integer)




