from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('signup.html')


@app.route('/mood')
def mood():
    return 'Welcome to Reddit Mood Checker!'


if __name__ == '__main__':
    app.run(debug=True)
