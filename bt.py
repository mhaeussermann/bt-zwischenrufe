# -*- coding: utf-8 -*-
import requests
import re
import os

#Get the PDF links to all protocols
base_url = "http://dip21.bundestag.de/dip21/btp/16/16"
url_list = []

for i in range(1,233):
    if i in range(1,10):
        url = base_url + "00" + str(i) + ".pdf"
        url_list.append(url)
    if i in range(10,100):
        url = base_url + "0" + str(i) + ".pdf"
        url_list.append(url)
    if i in range(100,236):
        url = base_url + str(i) + ".pdf"
        url_list.append(url)

d = os.path.dirname(os.path.abspath(__file__)) # directory of script
d2 = d + '/16/' # path to be created

try:
    os.makedirs(d2)
except OSError:
    pass

# Download the protocols
for item in url_list:
    response = requests.get(item)
    filename = item[item.rfind("/")+1:]
    print(filename)
    with open(d2 + filename, 'wb') as f:
        f.write(response.content)