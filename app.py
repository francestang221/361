from flask import (g, render_template, redirect,
                   url_for, request, flash)

from models import db, Customer, app


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = db
    g.db.engine.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request"""



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    flash('Please register or login.')
    if request.form:
        print(request.form)
        # create a new User object
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    print(request.form)
    return render_template('mood.html')


@app.route('/searches')
def searches():
    return render_template('searches.html')


if __name__ == '__main__':
    app.secret_key = 'secret'
    db.create_all()
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
