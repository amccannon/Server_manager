from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired, Length, EqualTo
from Application import app


#this code is used for creating a password and login using wtforms:
class RegisterNewUser(FlaskForm):
    """Registration"""

    firstname = StringField('firstName_label', validators=[InputRequired(message="FirstName Required"),
    Length(min=4, max=25, message="First Name must be between 4 and 25 characters")], 
    render_kw={"placeholder": "FirstName"})


    lastname = StringField('lastName_label',validators=[InputRequired(message="LastName Required"),
    Length(min=4, max=25, message="Last name must be between 4 and 25 characters")], 
    render_kw={"placeholder": "LastName"})


    email = StringField('email', validators=[InputRequired(message="Email Required"),
    Length(min=4, max=25, message="Email must be between 4 and 25 characters")], 
    render_kw={"placeholder": "Email"})


    password = PasswordField('password_label',validators=[InputRequired(message="Password Required"),
    Length(min=4, max=25, message="Password must be between 4 and 25 characters")], 
    render_kw={"placeholder": "Password"})


    confirm_pswd = PasswordField('confirm_pswd_label',validators=[InputRequired(message="Password Required"),
    EqualTo('password', message="Passwords must match")])


    assigned_team = StringField('assigned_team')


    create_user_button = SubmitField('Create')



