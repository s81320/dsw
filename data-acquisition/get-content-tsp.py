from newspaper import Article
import time
import sys , os
import json

# first filename
i=0


with open("links-tsp.txt" , "r") as link_file :
	all_lines = link_file.readlines()
	for link in all_lines:
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

		with open(filename + ".json", "w") as write_file:
		    json.dump(keep, write_file)

		with open(filename + ".txt", "w") as write_file:
			write_file.write(article.text)

		print("wrote " + str(i))

		
# keine direkte artikel id vorhanden, aber html dateien sind als nummern codiert
#  'url': 'https://www.tagesspiegel.de/politik/kommando-zurueck-was-gegen-die-wiedereinfuehrung-der-wehrpflicht-spricht/25978222.html',
# also einfach den dateinamen verwenden.
