from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField  
from wtforms.validators import DataRequired, URL, Optional, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired(), AnyOf(['cat', 'dog', 'porcupine'], message='Species must be cat, dog, or porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = TextAreaField('Notes')
    available = BooleanField('Available') 
