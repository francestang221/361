import requests
import json


def get_reddit(subreddit, topic):
    """GET REQUEST to get the Json Data of Reddit Posts"""
    query = ""
    for char in topic:
        if char == " ":
            query += "%20"
        else:
            query += char
    request = None
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/search/.json?q={topic}&source=recent&restrict_sr=1'
        request = requests.get(base_url, headers={'User-agent': 'osu_project'})
    except requests.ConnectionError:
        print('Connection Error. Please try again later.')
    return request.json()


def reddit_scraper(subreddit, topic):
    r = get_reddit(subreddit, topic)
    dict1 = r['data']['children']
    n = 1
    result = {"text": ""}
    num_of_posts = len(dict1) if len(dict1) <= 10 else 10
    for i in range(num_of_posts):
        dict2 = dict1[i]
        result['text'] += "# {}:".format(n) + dict2['data']['title']
        # result += "link to post: " + dict2['data']['permalink']
        result['text'] += dict2['data']['selftext']
        n += 1
    return json.dumps(result)
