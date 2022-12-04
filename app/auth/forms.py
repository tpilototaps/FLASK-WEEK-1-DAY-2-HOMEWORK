from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonSummons(FlaskForm):
    pokename = StringField('Pokemon name', validators=[DataRequired()])
    submit = SubmitField()