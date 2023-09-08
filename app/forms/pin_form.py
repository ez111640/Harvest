from flask_wtf import FlaskForm
from wtforms import StringField, URLField
from wtforms.validators import DataRequired
from app.models import Pin

class PinForm(FlaskForm):
    url=URLField('name', validators=[DataRequired()])
    link=URLField('link', validator=[DataRequired()])
    description=StringField('description')
    title=StringField('title')
