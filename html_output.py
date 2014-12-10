#!/usr/bin/python

def header():
	print("<!doctype html>")
	print("<html lang='en'>")
	print("<head>")
	print("<meta charset='utf-8'>")
	print("<style type='text/css'>")
	print("div.timestamp {width: 150px; float: left; font-size: small; font-family: monospace;}")
	print("img.icon {width: 16px; height: 16px;}")
	print(".debug {display: none;}")
	print("</style>")
	print("</head>")
	print("<body>")

def unnumberedlist(outputlist):
	print("<ul>")
	for i in outputlist:
#		icon = i[3].decode('utf-8').find("/", 8)
#		icon =(i[3].decode('utf-8')[:int(i[3].decode('utf-8').find("/", 8))+1]+"favicon.ico")
		icon = iconByLink(i[3].decode('utf-8'))
		print("<li><div class=timestamp>%02d.%02d.%04d %02d:%02d:%02d</div> <img class='icon' src='favicon/%s'> <a href=%s>%s</a></li>" % (i[1].tm_mday,i[1].tm_mon, i[1].tm_year, i[1].tm_hour, i[1].tm_min, i[1].tm_sec, icon, i[3],i[2])).encode('utf-8')
		print("")
	print("</ul>")

def iconByLink(link=None):
	icons = [] 
	icons.append(("events.ccc.de", "ccc.ico"))
	icons.append(("hackaday.com", "hackaday.ico"))
	icons.append(("netzpolitik.org", None))
	icons.append(("rss.feedsportal.com", "golem.ico"))
	icons.append(("rss.slashdot.org", "slashdot.ico"))
	icons.append(("www.gulli.com", None))
	icons.append(("www.heise.de", "heise.ico"))
	icons.append(("www.ka-news.de", "ka-news.ico"))
	icons.append(("www.spiegel.de", "spon.ico"))
	icons.append(("www.taz.de", "taz.ico"))
	icons.append(("www.zeit.de", "zeit.ico"))
	icons.append(("www.faz.net", "faz.ico"))
	icons.append(("www.theguardian.com", "guardian.ico"))

	if link:
		urlpart = link.split('/')
		foo = (icon for icon in icons if (icon[0] == urlpart[2]))
		for x in foo:
			return(x[1])

def footer():
	print("</body></html>")
