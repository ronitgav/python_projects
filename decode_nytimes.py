# -*- coding: utf-8 -*-

"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
"""

import requests
import urllib2
from bs4 import BeautifulSoup

count = 0
url = 'https://www.nytimes.com/'

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, 'lxml')
soup.prettify().encode('utf-8')

#elements = soup.find_all("story-heading")

for anchor in soup.select('.story-heading'):
    count += 1 
    if anchor.a != None:
        print('%d)  %s' % (count, anchor.a.text.replace('\n', '').strip()))
    else:
        print('%d)  %s' % (count, anchor.contents[0].strip()))


print('--------------------------------------------------------------')
print("There are %d articles on NYTimes.com " % count)
print('--------------------------------------------------------------')
