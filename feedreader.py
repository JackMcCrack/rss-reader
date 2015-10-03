#/usr/bin/python

import feedparser
import time
import threading
import html_output
from operator import itemgetter

DEBUG = False
class Feed(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    name = "undefined"
    def setName(self, text):
        self.name = text
    def run(self):
        self.start = time.time()
        self.d = feedparser.parse(self.url)
        self.end = time.time()
        self.diff = self.end - self.start
        if DEBUG:
            print("{:.3f}".format(self.diff) + " s\t" + self.url)
        articles.append(self.d)

def iconbyurl(config, url=None):
    if url:
        get = (config for config in config if (config[2] == url))
        for x in get:
            return x[0]

feeds = []  #for each rss-feed one threade
config = [] #keeps config from input.txt
articles = []   #all articles from all feeds
output = [] #just pubished, title, link, feedurl

with open('/home/jack/RSS-Reader/input.txt', 'r') as f:
    for line in f:
        if not line.strip().startswith("#"):
            (icon, name, url) = line.split(None, 2)
            config.append((icon, name, url.strip()))
            feed = Feed(url.strip())
            feeds.append(feed)

if DEBUG:
    print(config)

for x in feeds:
    x.start()   #gather rss feed in a thread

for x in feeds:
    x.join()    #wait for of all threads to finish

for post in articles:
    for x in post.entries:
        if hasattr(x, 'published_parsed') and hasattr(x, 'title_detail'):
            output.append((
                x.published_parsed,
                x.title,
                x.link,
                iconbyurl(config, x.title_detail.base),
                x.title_detail.base
            ))

output = sorted(output, key=itemgetter(0), reverse=True)

html_output.header(config)
html_output.selectionbox(config)
html_output.unnumberedlist(output)
html_output.footer()
