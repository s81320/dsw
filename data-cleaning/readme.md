# check lecture 1 : data quality dimensions ####

* correctness, 
* consistency: duplicates, invalid values 
* statistical properties: length of text, nr of words, 
* completeness: how many missing values

check automatic data quality testing: https://github.com/awslabs/deequ


# data testing

what to do for data cleaning:
* check for date of publication. If missing value, set it to the day it was scraped.
* check if something is not an 'article', according to meta data.
* if not article: remove it.
* check the length of the article. if it is too short (define by number of words): remove it.

* check for missing values of authors. imputation: if no person name is given, put in the name of the newspaper (impute)


# spell checking

* check for misspelled words and correct them, see lecture 3 

from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np

# compute hashed character ngram counts
vect = HashingVectorizer(analyzer='char_wb',ngram_range=(1,5),n_features=2**20, binary=True)
correct_words_ngrams = vect.transform(correct_words)
misspelled_words_ngrams = vect.transform(misspelled_words)
# compute string similarity between correct and misspelled words
similarity = correct_words_ngrams.dot(misspelled_words_ngrams.T)
# find most similar correct word for each misspelled word
most_similar_correct_word = similarity.toarray().argsort(axis=0)[-1,:]
corrections = [(word,correct_words[most_similar_correct_word[idx]]) for idx, word in enumerate(misspelled_words)]
corrections[:10]
# replace misspelled values in pandas Series with corrected ones
to_replace, replacement = zip(*corrections)
s = s.replace(to_replace, replacement)
s