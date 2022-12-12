from flask import render_template, request, url_for, flash, session, redirect
from app import app, db
""" from flask_login import login_user, current_user, logout_user, login_required, LoginManager """
from app.models import Employee, User
from app.functions import *
from app.forms import EmpForm

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
    form = EmpForm()

    """ if request.method == 'GET':
        employees = get_employee()
        len = employees.count
        return render_template('employee.html',title="Employee",len=len, employees=employees) """
    if request.method == 'POST':
        emp_name = request.form.get('emp_name')
        emp_subject = request.form.get('emp_subject')
        emp_phone = request.form.get('emp_phone')
        emp_email = request.form.get('enp_email')
        emp = Employee(emp_name=emp_name, emp_subject=emp_subject,
                            emp_phone=emp_phone, emp_email=emp_email)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('emp'))
    employees = get_employee()
    return render_template('employee.html',title="Сотрудники", form=form, len=29, employees=employees)


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