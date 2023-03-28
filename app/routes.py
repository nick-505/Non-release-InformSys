from flask import render_template, request, url_for, flash, session, redirect
from app import app
from .models import Employee, User, Lessons, Student, Subject, db
from .forms import EmpForm, LoginForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required  

## LOGIN ##
# User Managment
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## LOGIN/LOGOUT ##
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('les'))
    form = LoginForm()

    if request.method == 'POST':
        # get form data
        form_username = request.form["login_username"]
        form_pass = request.form["login_pass"]

    if form.validate_on_submit():
        user = User.query.filter_by(username=form_username).first()
        if user is not None: password = user.password
        if user is None or password != form_pass:
            flash("Неправильный логин или пароль")
            return redirect(url_for('login'))
        login_user(user)
        session.permanent = True
        return redirect(url_for('les'))
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('les'))

# Этот маршрут перенаправляет неавторизованных пользователей на страницу входа в систему
@login_manager.unauthorized_handler
def unauthorized():

    return redirect(url_for('login'))

## INDEX/УРОКИ ##
@app.route('/')
@app.route('/lessons', methods=['POST', 'GET'])
@login_required
def les():
    lessons = Lessons.query.order_by(Lessons.id)
    return render_template('index.html', title="Занятия", lessons=lessons)

@app.route('/emp', methods=['POST', 'GET'])
@login_required
def emp():
    form = EmpForm()

    if request.method == 'POST':

        subjects_list = []
        for data in request.form.getlist('mycheckbox'):
            subject = Subject.query.filter_by(subject_name=data).first()
            subjects_list.append(subject)

        employee = Employee (
            fio = request.form["emp_fio"],
            subjects = subjects_list,
            phone = request.form["emp_phone"],
            email = request.form["emp_email"]
        ) 

        db.session.add(employee)
        db.session.commit()

        return redirect(url_for('emp'))
    
    employees = Employee.query.order_by(Employee.fio)
    subjects = Subject.query.order_by(Subject.subject_name)

    return render_template('employee.html',title="Сотрудники", form=form, employees=employees, subjects=subjects)


