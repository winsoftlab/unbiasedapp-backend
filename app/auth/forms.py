from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired,Length,Regexp,EqualTo
from ..models import User
from wtforms import ValidationError


# login and Sign Up


class LoginForm(FlaskForm):
    email = StringField('Email',
                         id='email_login',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")

    submit =SubmitField('Log In')


class SignUpForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0, 'Username must have only letters,numbers, dots or underscores')])

    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Length(1,64), Email()])


    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired(), EqualTo('password2', message='Paswords must match.')])

    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')