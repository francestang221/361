from flask import Flask, g, render_template, flash, redirect, url_for
from flask_login import LoginManager
import forms
import models2

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'secret'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models2.User.get(models2.User.id == userid)
    except models2.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request """
    g.db = models2.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


# Views
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        models2.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index2'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return render_template('index2.html')


if __name__ == '__main__':
    models2.initialize()
    try:
        models2.User.create_user(
            username='frances',
            email='frances@goog.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass
    app.run(DEBUG=DEBUG, host=HOST, port=PORT)