from urllib.request import urlopen
from bs4 import BeautifulSoup

test_scrape = urlopen('https://www.reddit.com/r/OSUOnlineCS/search?q=cs%20225&restrict_sr=1')

# create BS object
soup = BeautifulSoup(test_scrape.read(), 'html.parser')

data = soup.findAll()

print(data)