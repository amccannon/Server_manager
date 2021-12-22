from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from Application import app, models


def invalid_credentials(form, field):
    """Email and password checker"""

    email_entered = form.email.data
    password_entered = field.data 


    # Check email is valid

    #user_object = models.User.query.filter_by(email=email.data).first()
    #if user_object in None:
    #    raise ValidationError("Email or password is incorrect")
    #elif password_entered != user_object.password:
    #    raise ValidationError("Username or passowrd is not correct")

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

    # validating the email
    def validate_firstname(self, email):
        user_object = models.User.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("email already exists")
            


class LoginForm(FlaskForm):
    """Login Form"""

    email = StringField('email_label', validators=[InputRequired(message="Username required")])
    password = StringField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])
    confirm_pswd = StringField('email_label', validators=[InputRequired(message="Password required"), invalid_credentials])
    login_button = SubmitField('Login')



