import requests
import urllib.request
import time
import pandas as pd

from bs4 import BeautifulSoup

url= 'http://www.tagesspiegel.de'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('a')


link_list = []
for one_a in all_a:
    if ( one_a['href'][-5:]== '.html' ):
            if(one_a['href'][0:4]=='http') :
          	    link_list.append(one_a['href'])  
            else:
          	    link_list.append('https://www.tagesspiegel.de' + one_a['href'])

link_list = list(set(link_list))

print('wrote links to file: ' , len(link_list))

with open("links-tsp-2020-07-08.txt" , "w") as file:
	for link in link_list:
		file.write(link + '\n')

