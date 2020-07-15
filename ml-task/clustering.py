import os

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

import re

from textblob_de import TextBlobDE 

import glob
import pandas as pd

import matplotlib.pyplot as plt


def preprocessing_02 (text):
    #print(text)
    a = text.lower() # lower cases only
    b = re.sub("(\\W|\\d)"," ",a) #remove non-ascii and digits
    blob = TextBlobDE(b)
    return(blob.words.lemmatize()) # lemmatize for german



def read_articles_transform_to_df (path_to_text_files='../tagesspiegel/*.txt'):

	file_list=glob.glob(path_to_text_files)
	#file_list = glob.glob("../tagesspiegel/*.txt")
	#print(file_list)

	n = len(file_list)
	print(n , "files to work with.")

	#list_of_articles = []
	X = pd.DataFrame(columns=['file','text'])
	#print('df', X)

	for i in range(n):
		with open (file_list[i]) as file:
			text=file.read()
			X=X.append({'file':file_list[i] , 'text':text}, ignore_index=True)
	print(X.shape)
	return(X)

def barplot_for_clusters (km_object):
	
	n, bins, patches = plt.hist(km_object.labels_, km_object.n_clusters, facecolor='blue', alpha=0.5)
	plt.title('sizes of clusters')
	plt.ylabel('nr. of articles')
	plt.show()

X = read_articles_transform_to_df()

list_of_articles = X['text']

cv = TfidfVectorizer(max_df=0.8 , min_df = 2)
km =  KMeans(init='k-means++', n_clusters=5, n_init=10)

text_cluster = Pipeline([('vect', cv), ('cluster', km) ])

#text_cluster.fit(list_of_articles[0:20])
text_cluster.fit(list_of_articles)

labels_as_column = pd.DataFrame(km.labels_)
print(type(labels_as_column), labels_as_column.shape)

X['cluster'] = pd.DataFrame(km.labels_) # contains labels
print(X)

barplot_for_clusters(km)

# make it a new column in DataFrame X
