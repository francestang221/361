import json
import requests
import RedditScraper
from flask import Flask, render_template, flash, request


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'secret'


"""
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")

        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
    return render_template('register.html', form=form)
"""


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    if request.method == "POST":
        subreddit = request.form.get("subreddit")
        topic = request.form.get("topic")
        try:
            data = RedditScraper.reddit_scraper(subreddit, topic)
            display_data = json.loads(data)['text']
            if topic == "":  # error 1: user didnt' enter topic
                display_data = f"You didnt enter a topic for r/{subreddit}. "
            elif display_data == "":    # error 2: no result
                display_data = "No results found :/"

            # get the mood result
            mood_url = "https://cs361-sentiment.herokuapp.com/tones"
            response = requests.post(mood_url, data=data)
            sentiments = json.loads(response.content)
            if len(sentiments) == 0:  # error 3: no sentiment
                sentiments = ["*___*"]
            return render_template('mood.html', data=display_data, sentiments=sentiments)
        except KeyError:
            return render_template('error.html')
    return render_template('mood.html')


"""
@app.route('/searches')
def view_searches():
    return render_template('searches.html')
"""


@app.route('/resources')
def resources():
    return render_template('learn.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # initialize DB
    app.run()
