from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('signup.html')


@app.route('/mood')
def mood():
    return  render_template('mood.html')


@app.route('/searches')
def searches():
    return render_template('searches.html')


if __name__ == '__main__':
    app.run(debug=True)
