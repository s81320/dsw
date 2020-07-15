import requests
import urllib.request
import time
import pandas as pd

from bs4 import BeautifulSoup

link_list=[]

url= 'https://www.sueddeutsche.de/politik'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('a')

print("found: " , len(all_a))


for one_a in all_a:
	try:
		if(one_a['href'].startswith('https://www.sueddeutsche.de/politik/')):
			link_list.append(one_a['href'])
	except:
		pass


url= 'https://www.sueddeutsche.de/wirtschaft'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('a')

print("found: " , len(all_a))

for one_a in all_a:
	try:
		if(one_a['href'].startswith('https://www.sueddeutsche.de/wirtschaft/')):
			link_list.append(one_a['href'])
	except:
		pass


url= 'https://www.sueddeutsche.de/leben'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('a')

print("found: " , len(all_a))

for one_a in all_a:
	try:
		if(one_a['href'].startswith('https://www.sueddeutsche.de/leben/')):
			link_list.append(one_a['href'])
	except:
		pass



link_list = list(set(link_list))

print('wrote links to file: ' , len(link_list))

with open("links-sz-2020-07-13.txt" , "a+") as file:
	for link in link_list:
		file.write(link + '\n')

# link types collected from beautiful soup

