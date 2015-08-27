#!/usr/bin/python
from operator import itemgetter


def header(icons=None):
	print("<!doctype html>")
	print("<html lang='en'>")
	print("<head>")
	print("<meta charset='utf-8'>")
	print("<style type='text/css'>")
	print("div.timestamp {float: left; font-size: small; font-family: monospace;}")
	print("div.icon {margin: 0 3px 0 12px; width: 16px; height: 16px; float: left;}")
	for i in list(set(map(itemgetter(0),icons))):
		print("div.icon.%s {background-image: url('./favicon/%s.ico');}" % ( i, i))
	
	print("div.icon.feed {background-image: url('./favicon/Feed-icon_16x16.svg');}")
	print("ul {list-style-type: none;}")
	print("li a:before{ content: ''; position: absolute; z-index: -1; right: 100%; bottom: 0; background: #2098d1; height: 2px; -webkit-transition-property: right; transition-property: right; -webkit-transition-duration: 0.3s; transition-duration: 0.3s; -webkit-transition-timing-function: ease-out; transition-timing-function: ease-out; }")
	print("li a{text-decoration: none; display: inline-block; vertical-align: middle; -webkit-transform: translateZ(0); transform: translateZ(0); box-shadow: 0 0 1px rgba(0, 0, 0, 0); -webkit-backface-visibility: hidden; backface-visibility: hidden; -moz-osx-font-smoothing: grayscale; position: relative; overflow: hidden; }")
	print("li a:hover:before, li a:focus:before, li a:active:before {left: 0px; right: 0px;}")
	print(".debug {display: none;}")
	print(".selection {float: right; width: 300px; position: fixed; left: auto; right: 0px; top: 0px;}")
	print("div.selection {display: none;}")
	print(".selection div.icon {float: left; margin: 0px 3px 0px 0px;}")
	print(".selection li div:not(.icon) {text-decoration: underline;}")
	print(".hidden {display: none;}")
	print("</style>")
	print("<script src='/jquery-2.1.4.min.js'></script>")
	print("<script src='/jquery-dateFormat.min.js'></script>")
	print("<script type='text/javascript'>")
	print("$(document).ready(function(){")
	print("  $('.timestamp').each(function (idx, elem) {jQuery(elem).text(jQuery.format.toBrowserTimeZone(jQuery(elem).text(), 'dd.MM.yyyy HH:mm:ss'))});")
	print("  $('div.selection').show()")
	print("  $('div.selection li.feed div').click(function(e,ui){var foo=$(this).attr('class'); $('li.'+foo).toggleClass('hidden') })")
	print("});")
	print("</script>")
	print("</head>")
	print("<body>")


def selectionbox(config):
        print("<div class='selection'>")
        print("<ul>")
	tmp = list(set(map(itemgetter(0,1), config)))
	for i in tmp:
		print("  <li class='feed'><div class='icon %s'></div><div class='%s'>%s</div></li>" %( i[0], i[0], i[1] ))
        print("</ul>")
        print("</div>")


def unnumberedlist(outputlist):
	print("<div><ul>")
	last = None
	for i in outputlist:
		if last:
			current = ((i[0].tm_year, i[0].tm_mon, i[0].tm_mday, i[0].tm_hour, i[0].tm_min, i[0].tm_sec))
			if last[0:3] != current[0:3]:
				print("</ul></div><hr><div><ul>")
			elif last[0:4] != current[0:4]:
				print("</ul><ul>")
				
		print("<li class='%s'><div class='timestamp'>%04d-%02d-%02dT%02d:%02d:%02dZ</div> <div class='icon %s'></div> <a href='%s'>%s</a></li>" % (i[3], i[0].tm_year,i[0].tm_mon, i[0].tm_mday, i[0].tm_hour, i[0].tm_min, i[0].tm_sec, i[3], i[2],i[1])).encode('utf-8')
		last = ((i[0].tm_year, i[0].tm_mon, i[0].tm_mday, i[0].tm_hour, i[0].tm_min, i[0].tm_sec))
	print("</ul></div>")


def footer():
	print("</body></html>")

