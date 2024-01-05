import sys
from urllib.request import urlopen

domains = ""

url = "https://duckduckgo.com/?t=ftsa&q=" + sys.argv[1]

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)
