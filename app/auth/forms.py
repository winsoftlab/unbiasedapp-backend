from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


# login and Sign Up


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")

    submit = SubmitField("Log In")


class SignUpForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(5, 64),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Username must have only letters,numbers, dots or underscores",
            ),
        ],
    )

    email = StringField("Email", validators=[DataRequired(), Length(5, 64), Email()])

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("password2", message="Paswords must match."),
        ],
    )

    password2 = PasswordField("Confirm password", validators=[DataRequired()])

    submit = SubmitField("Sign Up")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")


class DeleteAccountForm(FlaskForm):
    answer = StringField('Enter "email" to delete', validators=[DataRequired()])
    submit = SubmitField("Delete account")
