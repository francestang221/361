import RedditScraper
import requests

data = RedditScraper.reddit_scraper('OSUOnlineCS', 'CS 225')

print(data)

mood_url = "https://cs361-sentiment.herokuapp.com/tones"
response = requests.post(mood_url, data=data)
print(response.content)