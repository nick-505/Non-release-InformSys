from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from .models import Employee

##Employee Form##
class EmpForm(FlaskForm):
    emp_fio = StringField('Имя', validators=[DataRequired()])
    emp_phone = StringField('Телефон', validators=[DataRequired()])
    emp_email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Добавить')

##Login Form##
class LoginForm(FlaskForm):
    login_username = StringField('Логин пользователя')
    login_pass = PasswordField('Пароль пользователя')

    submit = SubmitField('Войти')

##Request Form##
class RequestForm(FlaskForm):
    stud_fio = StringField('Имя студента', validators=[DataRequired()])
    stud_phone = StringField('Телефон студента', validators=[DataRequired()])
    stud_email = StringField('Эл. почта студента', validators=[DataRequired()])

    emp_name = SelectField('Имя репетитора', validators=[DataRequired()])

    submit = SubmitField('Отправить')

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.emp_name.choices = [(c.id, c.fio) for c in Employee.query.all()]
