from flask.sessions import NullSession
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from Application import models
from passlib.hash import pbkdf2_sha256



def invalid_credentials(form, field):
    """Email and password checker"""

    email_entered = form.email.data
    password_entered = field.data 


    # Check email is valid
    user_object = models.User.query.filter_by(email=email_entered).first()
    if user_object == None:
        raise ValidationError("Email or password is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Email or password is incorrect")


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


    teams = StringField('teams')


    create_user_button = SubmitField('Create')

    # validating the email with a custom Validator 
    def validate_email(self, email):
        user_object = models.User.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already exists. Select a different email.")

    #validating on teams with a custom Validator
    def validate_teams(self, teams):
        user_object = models.User.query.filter_by(teams=teams.data).first()
        if user_object:
            raise ValidationError("Tean already exists. Add to a different team.")
            


class LoginForm(FlaskForm):
    """Login Form"""

    email = StringField('email_label', validators=[InputRequired(message="Email required")])
    password = StringField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])
    login_button = SubmitField('Login')

