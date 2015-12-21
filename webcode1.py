# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
countIn = raw_input('Enter count: ')
posIn = raw_input('Enter position: ')

count = int(countIn)-1
position = int(posIn)-1

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
"""for tag in tags:"""
for i in range(count):
    newurl = tags[position].get('href')
    print "Retrieving: ", newurl
    nhtml = urllib.urlopen(newurl).read()
    soup = BeautifulSoup(nhtml)
    tags = soup('a')
print "Last Url: ",tags[position].get('href')
print tags[position].contents[0]
