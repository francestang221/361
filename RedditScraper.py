from urllib.request import urlopen
from bs4 import BeautifulSoup

subreddit = 'OSUOnlineCS'
keyword = 'CS 225'


def parse_keyword(kw):
    ans = ""
    for i in kw:
        if i == " ":
            ans += "%20"
        else:
            ans += i
    return ans


query = parse_keyword(keyword)

test_scrape = urlopen('https://www.reddit.com/r/' + subreddit + '/search?q=' + query + '&restrict_sr=1')

# create BS object
soup = BeautifulSoup(test_scrape.read(), 'html.parser')

data = soup.prettify()

print(data)

# "title"
# "permalink"

