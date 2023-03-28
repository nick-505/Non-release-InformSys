from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
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
