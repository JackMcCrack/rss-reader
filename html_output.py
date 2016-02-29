#!/usr/bin/env python2
from operator import itemgetter
import hashlib

def header(icons=None):
    print("<!doctype html>")
    print("<html lang='en'>")
    print("<head>")
    print("<meta charset='utf-8'>")
    print("<link rel='stylesheet' href='rss-reader.css'>")
    print("<style type='text/css'>")
    for i in list(set(map(itemgetter(0), icons))):
        print("div.icon.%s {background-image: url('./favicon/%s.ico');}" % (i, i))
    print("</style>")
    print("<script src='/jquery-2.1.4.min.js'></script>")
    print("<script src='/jquery-dateFormat.min.js'></script>")
    print("<script type='text/javascript'>")
    print("$(document).ready(function(){")
    print("  $('.timestamp').each(function (idx, elem) {jQuery(elem).text(jQuery.format.toBrowserTimeZone(jQuery(elem).text(), 'dd.MM.yyyy HH:mm:ss'))});")
    print("  $('div.selection').show()")
    print("  $('div.selection li.select input[type=checkbox]').click(function(e,ui){var foo=$(this).attr('name'); $('li.'+foo).toggleClass('hidden') })")
    print("});")
    print("</script>")
    print("</head>")
    print("<body>")


def selectionbox(config):
    print("<div class='selection'>")
    print("<ul>")
    tmp = list(set(map(itemgetter(0, 1, 2), config)))
    tmp = sorted(tmp, key=itemgetter(2))
    for i in tmp:
        print("  <li class='select'><input type='checkbox' name='%s' checked></input><div class='icon %s'></div><div class='%s'>%s</div></li>" % (
            hashlib.md5(i[2]).hexdigest(),
            i[0],
            i[0],
            i[1]
        ))

        print("</ul>")
        print("</div>")


def unnumberedlist(outputlist):
    print("<div><ul>")
    last = None
    for i in outputlist:
        if last:
            current = ((
                i[0].tm_year,
                i[0].tm_mon,
                i[0].tm_mday,
                i[0].tm_hour,
                i[0].tm_min,
                i[0].tm_sec
            ))

            if last[0:3] != current[0:3]:
                print("</ul></div><hr><div><ul>")
            elif last[0:4] != current[0:4]:
                print("</ul><ul>")

        print("<li class='%s'><div class='timestamp'>%04d-%02d-%02dT%02d:%02d:%02dZ</div> <div class='icon %s'></div> <a href='%s'>%s</a></li>" % (
            hashlib.md5(i[4]).hexdigest(),
            i[0].tm_year,
            i[0].tm_mon,
            i[0].tm_mday,
            i[0].tm_hour,
            i[0].tm_min,
            i[0].tm_sec,
            i[3],
            i[2],
            i[1])).encode('utf-8')

        last = ((
            i[0].tm_year,
            i[0].tm_mon,
            i[0].tm_mday,
            i[0].tm_hour,
            i[0].tm_min,
            i[0].tm_sec
        ))

    print("</ul></div>")


def footer():
    print("</body></html>")

