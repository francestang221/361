from flask import (render_template,
                   url_for, request)

from models import db, Customer, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.form)
    return render_template('signup.html')


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    print(request.form)
    return render_template('mood.html')


@app.route('/searches')
def searches():
    return render_template('searches.html')


if __name__ == '__main__':
    app.run(debug=True)
