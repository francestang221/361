import json

import requests

import RedditScraper
import forms
from flask import Flask, render_template, flash

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        """
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        """
    return render_template('register.html', form=form)


# WIP
@app.route('/mood', methods=['GET', 'POST'])
def mood():
    form = forms.RedditForm()
    if form.validate_on_submit():
        subreddit = form.subreddit.data
        topic = form.topic.data
        # WIP: need to display in a scroll box
        data = RedditScraper.reddit_scraper(subreddit, topic)
        display_data = json.loads(data)['text']
        # get the mood result
        mood_url = "https://cs361-sentiment.herokuapp.com/tones"
        response = requests.post(mood_url, data=data)
        sentiments = json.loads(response.content)
        return render_template('mood.html', data=display_data, sentiments=sentiments, form=form)
    return render_template('mood.html', form=form)


@app.route('/searches')
def view_searches():
    return render_template('searches.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
