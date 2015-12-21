import urllib
import re
from bs4 import BeautifulSoup

html = urllib.urlopen('https://spaceflightnow.com/launch-schedule/').read()

soup = BeautifulSoup(html)


name = soup.find_all("span", class_="mission")
date = soup.find_all("span", class_="launchdate")


for i,j in zip(date,name):
    str1 = re.findall('>([^<]*)',str(j))
    str2 = str(i.get_text())
    if str2.startswith("Dec"):
        print str2," : ",str1[0]
    else:
        pass
