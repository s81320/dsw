from newspaper import Article
import time
import sys , os
import json

# first filename witt be i+1
# so i should be the latest number given to an article
i=529 # for 14th of July


with open("links-tsp-2020-07-14-new.txt" , "r") as link_file :
	all_lines = link_file.readlines()
	for link in all_lines:
		link = link.replace('\n', '')
		article = Article(link)
		article.download()
		time.sleep(2)
		article.parse()
		article.nlp()
		article.fetch_images()

		## generate a filename
		i=i+1
		filename = f'{i:05}'
		# should check, if file exists ...

		keep = article.meta_data['og']
		keep['authors'] = article.authors
		keep['text-link'] = filename
		keep['images-link'] = list(article.images)
		keep['publish-date'] = str(article.publish_date)
		keep['paper'] = 'tagesspiegel'
		keep['id'] = link[-13:-5]
		#keep['id'] = link
		keep['text'] = article.text

		json_txt = json.dumps(keep, indent=4) # dumps , before used dump . What's the difference??
		with open(filename + ".json", 'w', encoding='utf-8') as file:
			file.write(json_txt)
		
		print("wrote " + str(i))

# 8.7. added the article id as the numbers in the filename 8888888.html
# added the title to the text file, so the text file now contains the title and the text.
		
# keine direkte artikel id vorhanden, aber html dateien sind als nummern codiert
#  'url': 'https://www.tagesspiegel.de/politik/kommando-zurueck-was-gegen-die-wiedereinfuehrung-der-wehrpflicht-spricht/25978222.html',
# also einfach den dateinamen verwenden.
