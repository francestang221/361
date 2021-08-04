from flask import jsonify
from flask_restful import Resource, Api
import RedditScraper

import models


class RedditData(Resource):
    def get(self, subreddit, topic):
        # scraped reddit post
        data = RedditScraper.reddit_scraper(subreddit, topic)
        return data
