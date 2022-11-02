from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, FloatField,BooleanField, IntegerField,TextAreaField
from wtforms.validators import InputRequired,Optional, AnyOf,URL, NumberRange

class PetForm(FlaskForm):
    species_values=['dog','cat','porcupine']
    name=StringField("Name", validators=[InputRequired(message="Name cannot be blank")])
    species=StringField("Species", validators=[InputRequired(message="Species cannot be blank"),AnyOf(species_values,message="Must be a cat, dog or porcupine")])
    photo_url=StringField("Link to photo",validators=[Optional(),URL(message="Must be valid URL")])
    age=IntegerField("Age",validators=[Optional(), NumberRange(min=0,max=30,message="Must be between 0 and 30")])
    notes=TextAreaField("Notes",validators=[Optional()])
    available=BooleanField("Available", validators=[Optional()])