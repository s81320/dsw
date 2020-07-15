# not working at the moment.
# articles are not downloaded or title is not printed.

from newspaper import Article
import time
import sys , os
import json

# first filename witt be i+1
# so i should be the latest number given to an article
i=0


with open("links-sz-2020-07-13.txt" , "r") as link_file :
	all_lines = link_file.readlines()
	for link in all_lines[0:3]: # for debugging, only run the first three links
		article = Article(link)
		print(i , ": ", link)
		article.download()
		print("title: " , article.title)
		time.sleep(2)
		article.parse()
		article.nlp()
		article.fetch_images() # I am not working with images at the moment

		## generate a filename
		i=i+1
		filename = f'{i:05}'
			# should check, if file exists ...

		keep = article.meta_data['og']
		keep['authors'] = article.authors
		keep['text-link'] = filename
		keep['images-link'] = list(article.images)
		keep['publish-date'] = str(article.publish_date)
		keep['paper'] = 'sueddeutsche'
		keep['id'] = link[-1:-9]

		with open(filename + ".json", "w") as write_file:
			json.dump(keep, write_file)

		with open(filename + ".txt", "w") as write_file:
			write_file.write(article.title + '\n' +  article.text)

		print("wrote " + str(i))

# 8.7. added the article id as the numbers in the filename 8888888.html
# added the title to the text file, so the text file now contains the title and the text.
		
# keine direkte artikel id vorhanden, aber html dateien sind als nummern codiert
#  'url': 'https://www.tagesspiegel.de/politik/kommando-zurueck-was-gegen-die-wiedereinfuehrung-der-wehrpflicht-spricht/25978222.html',
# also einfach den dateinamen verwenden.
