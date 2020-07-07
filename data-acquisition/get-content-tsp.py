from newspaper import Article
import time
import sys , os
import json

#article = Article('https://www.nytimes.com/2020/07/06/us/Epidemiologists-coronavirus-protests-quarantine.html?action=click&module=Top%20Stories&pgtype=Homepage')
#article.download()
#article.parse()
#print(article.authors)
#print(article.text)

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

		#with open(filename, 'w') as output_file:
		#	output_file.write('paper: tagesspiegel ' + '\n')
		#	output_file.write('source: ' + link + '\n')
		#	if(len(article.authors)==0):
		#		output_file.write("author: none\n")
		#	else:
		#		output_file.write("author: " )
		#		for author in article.authors:
		#			output_file.write(author + ', ')
		#	output_file.write("\n")
		#	output_file.write('title: ' + article.title + '\n')
		#	output_file.write("publication_date: " + str(article.publish_date )+ '\n')
		#	output_file.write('articleid: ' + str(article.meta_data['articleid'])+ '\n')
		#	output_file.write('image: ' + article.top_image + '\n')
		#	output_file.write('text: ' + article.text + '\n')
		#	print("done" + str(i))

# keine direkte artikel id vorhanden, aber html dateien sind als nummern codiert
#  'url': 'https://www.tagesspiegel.de/politik/kommando-zurueck-was-gegen-die-wiedereinfuehrung-der-wehrpflicht-spricht/25978222.html',
# also einfach den dateinamen verwenden.
