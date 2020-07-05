import requests
import urllib.request
import time
import pandas as pd

from bs4 import BeautifulSoup

url= 'https://www.siegessaeule.de/magazin'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('a')


link_list = []
for one_a in all_a:
    if(one_a['href'][0:9]=='/magazin/') :
        link_list.append('https://www.siegessaeule.de'+one_a['href'])  
        
link_list = list(set(link_list))

print('wrote links to file: ' , len(link_list))

with open("links-siegessaeule.txt" , "a+") as file:
	for link in link_list:
		file.write(link + '\n')