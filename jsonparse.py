import json
import urllib

input = raw_input('Enter Url: ')

url = urllib.urlopen(input)
data = url.read()
jsondata = json.loads(str(data))
print 'Retrieving json: ', json.dumps(jsondata, indent=4)
sum = 0

comments = jsondata["comments"]

for user in comments :
    sum+= user["count"]
print 'sum = ', sum
