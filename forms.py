from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers and underscores only.")
            ),
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            # Email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


class RedditForm(FlaskForm):
    subreddit = StringField(
        'Subreddit',
        validators=[DataRequired()])

    topic = StringField(
        'Topic',
        validators=[DataRequired()])
