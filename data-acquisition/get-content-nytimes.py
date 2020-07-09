from newspaper import Article
import time
import sys , os

import json

#article = Article('https://www.nytimes.com/2020/07/06/us/Epidemiologists-coronavirus-protests-quarantine.html?action=click&module=Top%20Stories&pgtype=Homepage')
#article.download()
#article.parse()
#print(article.authors)
#print(article.text)

# first filename will be i+1
i=40



with open("links-nytimes-2020-07-08-new.txt" , "r") as link_file :
	all_lines = link_file.readlines()
	for link in all_lines:
		article = Article(link)
		article.download()
		time.sleep(2)
		article.parse()
		article.nlp()
		article.fetch_images()

		i=i+1
		filename = f'{i:05}'

		keep = article.meta_data['og']
		keep['authors'] = article.authors
		keep['text-link'] = filename
		keep['images-link'] = list(article.images)
		keep['publish-date'] = str(article.publish_date)
		keep['paper'] = 'nytimes'

		with open(filename + ".json", "w") as write_file:
		    json.dump(keep, write_file)

		with open(filename + ".txt", "w") as write_file:
			write_file.write(article.title+'\n'+article.text)

		print("wrote " + str(i))


######
#Meta data at ny times
#keep 'og' dict of meta_data, containing
#url , type , title, image {identifyer: ...  , alt: ... } , description 

# note that the nyt meta data gives us an image with a description.

# we add authors, a link to the text file for the text of the article , images_link (may be a list of urls) ,  
# publish date and name of the paper (nytimes)