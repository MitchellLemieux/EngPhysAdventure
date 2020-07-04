import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen("http://pythonprogramming.net").read()

    print(x)
except Exception as e:
    print((str(e)))
