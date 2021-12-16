from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.validators import InputRequired, Length, EqualTo
from Application import app



class RegisterNewUser(FlaskForm):
    """Registration"""

    firstname = StringField('firstName_label', validators=[InputRequired(message="FIrstName Required"),
    Length(min=4, max=25, message="First Name must be between 4 and 25 characters")], render_kw={"placeholder": "FirstName"})
    lastname = StringField('lastName_label')
    email = StringField('email')
    password = PasswordField()
    confirm_pswd = PasswordField('confirm_pswd_label')
    assigned_team = StringField('assigned_team')