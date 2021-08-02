import requests


def get_reddit(subreddit, topic):
    query = ""
    for char in topic:
        if char == " ":
            query += "%20"
        else:
            query += char
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/search/.json?q={topic}&source=recent&restrict_sr=1'
        request = requests.get(base_url, headers={'User-agent': 'osu_project'})
    except:
        print('An Error Occured')
    return request.json()


def reddit_scraper(subreddit, topic):
    r = get_reddit(subreddit, topic)
    dict1 = r['data']['children']
    n = 1
    num_of_posts = 5
    if len(dict1) < 5:
        num_of_posts = len(dict1)
    for i in range(num_of_posts):
        dict2 = dict1[i]
        if dict2['data']['selftext'] != "":
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('# {}:'.format(n), dict2['data']['title'])
            print("link to post: ", dict2['data']['permalink'])
            print(dict2['data']['selftext'])
            n += 1
    return 'I love pizza'   # will return a Dictionary of posts
