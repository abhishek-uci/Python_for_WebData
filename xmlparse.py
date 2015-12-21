import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')

uh = urllib.urlopen(address)
data = uh.read()
print data
tree = ET.fromstring(data)
sum = 0

results = tree.findall('comments/comment')

for num in results:
    sum+= int(num.find('count').text)
print 'sum = ',sum
