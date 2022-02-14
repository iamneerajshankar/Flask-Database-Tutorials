
from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField

from wtforms.validators import DataRequired, Length

class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    address = StringField("Address", validators=[DataRequired(), Length(max=300)])
    email = EmailField("Email", validators=[DataRequired(), Length(max=100)])