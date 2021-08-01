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
        request = requests.get(base_url, headers={'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()


subreddit = 'OSUOnlineCS'
topic = "CS 290"

r = get_reddit(subreddit, topic)

Dict = r['data']['children']
n = 1
for i in range(len(Dict)):
    d = Dict = r['data']['children'][i]
    if Dict['data']['selftext'] != "":
        print('**********')
        print('top {} post:'.format(n), Dict['data']['title'])
        print(Dict['data']['selftext'])
        n += 1
