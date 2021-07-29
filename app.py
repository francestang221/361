from flask import (render_template, redirect,
                   url_for, request)

from models import db, Customer, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.form:
        print(request.form)
        # create a new User object
        new_user = Customer(email=request.form['email'],
                            username=request.form['username'],
                            password=request.form['password'])

        db.session.add(new_user)
        db.session.commit()
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
    db.create_all()
    app.run(debug=True)
