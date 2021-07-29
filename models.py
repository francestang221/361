from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_login import UserMixin

# UserMixin: is_anonymous: return True for guest users

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

    def __repr__(self):
        return f'''<Customer (Username: {self.username}
                Email: {self.email}
                Password: {self.password})>
                '''

# create a Model for Searches: sub + keyword

