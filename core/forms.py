from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField, TextAreaField,
                    SelectField, DateField, RadioField)
from wtforms.validators import DataRequired, EqualTo, Length, Email
from wtforms.widgets.html5 import DateInput



class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender',choices=['Male','Female'])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()], widget=DateInput())
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_writer = RadioField('Are you a writer?',choices=['Yes','No'])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit')

    
class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender', choices=['Male', 'Female'])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()], widget=DateInput())
    submit = SubmitField('Update')
