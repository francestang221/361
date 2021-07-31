from peewee import *
import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('user.db')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(username=username,
                       email=email,
                       password=generate_password_hash(password),
                       is_admin=admin)
        except IntegrityError:
            raise ValueError('User already exists')


# for Save my Search / View My Saved Searches
class Search(Model):
    user_id = ForeignKeyField(User, related_name='search_set')
    subreddit = CharField()
    keyword = CharField
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Search], safe=True)
    DATABASE.close()