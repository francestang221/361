from flask import (Flask, render_template,
                   url_for, request)

app = Flask(__name__)


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
