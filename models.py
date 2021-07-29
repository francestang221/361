import datetime
from sqlalchemy.exc import IntegrityError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
db = SQLAlchemy(app)


class Customer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('Username', db.String(80), unique=True, nullable=False)
    email = db.Column('Email', db.String(120), unique=True, nullable=False)
    password = db.Column('Password', db.String(120), unique=False, nullable=False)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)

    class Meta:
        database = db
        order_by = ('-created',)

    @classmethod
    def create_user(cls, username, email, password):
        try:
            cls.create(username=username,
                       email=email,
                       password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError('User already exists')

    def __repr__(self):
        return f'''<Customer (Username: {self.username}
                Email: {self.email}
                Password: {self.password})>
                '''

# create a Model for Searches: sub + keyword

