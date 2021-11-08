from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, NumberRange


class SearchForm(FlaskForm):
    zipcode = IntegerField('Zipcode',validators=[DataRequired()])
    submit = SubmitField("Go")