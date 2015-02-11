#/usr/bin/python

import feedparser
import time
import threading
import html_output
from operator import itemgetter

DEBUG = False
class Feed (threading.Thread):
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
		

feeds = []
articles = []
output = []
f = open('./input.txt', 'r')


for line in f:
	feed = Feed(line.strip())
	feeds.append(feed)
f.close()

for x in feeds:
	x.start()

for x in feeds:
	x.join()
for post in articles:
	for x in post.entries:
		output.append((x.id, x.published_parsed, x.title, x.link))	
output = sorted(output, key=itemgetter(1), reverse=True)


html_output.header()
html_output.unnumberedlist(output)
html_output.footer()
