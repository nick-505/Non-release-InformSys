from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

##Employee Form##
class EmpForm(FlaskForm):
    emp_name = StringField('Имя', validators=[DataRequired()])
    emp_subject = StringField('Предмет', validators=[DataRequired()])
    emp_phone = StringField('Телефон', validators=[DataRequired()])
    emp_email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Добавить')

