from flask import render_template, request, url_for, flash, session
from app import app, db
""" from flask_login import login_user, current_user, logout_user, login_required, LoginManager """
from app.models import Employee, User
from app.functions import *

##LOGIN##
""" @login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager
 """

@app.route('/')
def index(): 
    return render_template('index.html', title="Home")

@app.route('/emp', methods=['POST', 'GET'])
def emp():
    if request.method == 'GET':
        employees = get_employee()
        len = employees.count
        return render_template('employee.html',title="Employee",len=len, employees=employees)
    elif request.method == 'POST':
        return "Hello"

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        

        """ field = request.form['field']
        value = request.form['value']
        editid = request.form['id']

        if field == 'name':
            sql = "UPDATE employees SET name=%s WHERE id=%s"
        if field == 'subject':
            sql = "UPDATE employees SET subject=%s WHERE id=%s"

        data = (value, editid) """


@app.route('/lessons', methods=['POST', 'GET'])
def les():
    return "HELLO"