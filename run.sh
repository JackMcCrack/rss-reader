/usr/bin/python /home/jack/RSS-Reader/feedreader.py >/tmp/news.html

if [ -s /tmp/news.html ]
then
	cat /tmp/news.html >/var/www/news.html
fi

