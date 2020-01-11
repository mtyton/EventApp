from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
import datetime


class EventAddForm(FlaskForm):
    name = StringField("event", validators=(DataRequired(),))
    date = DateField('date', validators=(DataRequired(),), default=datetime.date.today())
    submit = SubmitField('Add')


class LoginForm(FlaskForm):
    username = StringField("username", validators=(DataRequired(),))
    password = PasswordField("password", validators=(DataRequired(), Length(min=10)))
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField("username", validators=(DataRequired(),))
    password = PasswordField("password", validators=(DataRequired(), Length(min=10)))
    confirm_password = PasswordField("confirm", validators=(DataRequired(), Length(min=10)))
    email = StringField("email", validators=(DataRequired(),Email(),))