from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
import datetime


class EventAddForm(FlaskForm):
    name = StringField("event", validators=(DataRequired(),))
    date = DateField('date', validators=(DataRequired(),), default=datetime.date.today())
    submit = SubmitField('Add')