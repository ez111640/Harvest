from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import Board

class BoardForm(FlaskForm):
    name=StringField('name', validators=[DataRequired()])
