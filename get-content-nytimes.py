from newspaper import Article
import time

#article = Article('https://www.nytimes.com/2020/07/06/us/Epidemiologists-coronavirus-protests-quarantine.html?action=click&module=Top%20Stories&pgtype=Homepage')
#article.download()
#article.parse()
#print(article.authors)
#print(article.text)

with open("links-nytimes.txt" , "r") as link_file , open ("content-nytimes.txt" , "w") as content_file:
	all_lines = link_file.readlines()
	for link in all_lines:
		article = Article(link)
		article.download()
		time.sleep(2)
		article.parse()
		content_file.write("#########################")
		for author in article.authors:
			content_file.write(author+",")
		content_file.write("\n")
		content_file.write(article.text)

