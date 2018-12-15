# Scraping Chinese words containing 'Gold'
# Searching famous Chinese poems to find two words combination of 'Gold' + 'some word'
# Geting insipartion for baby names from those combinations


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

page = urllib.request.urlopen('http://www.cidianwang.com/bushou/140.htm', context=ctx).read()
soup = BeautifulSoup(page, 'html.parser')
tags = soup('a')
name = list()
for tag in tags:
    if len(tag.contents[0]) != 1:
        continue
    name.append(tag.contents[0])
name.append('金')


f = open('chuci.txt',encoding='UTF-8')
owen_name = open('name.txt','w')
for line in f:
    line = line.strip()
    for i in line:
        if i in name and len(line) < 80:
            print(line,'>>>',line.find(i),'>>>',i)
            print(line,'>>>',line.find(i),'>>>',i, file = owen_name)
f.close()
owen_name.close()
