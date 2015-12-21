import urllib
from BeautifulSoup import *

#  http://python-data.dr-chuck.net/comments_216194.html  input url
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
print soup
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
print tags

for tag in tags:
    print "Tag : ", tag
    num = tag.contents[0]
    sum+=int(num)
print sum
