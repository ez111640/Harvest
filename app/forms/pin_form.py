from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models import Pin

class PinForm(FlaskForm):
    url=StringField('name', validators=[DataRequired()])
    link=StringField('link', validators=[DataRequired()])
    description=StringField('description')
    title=StringField('title')
