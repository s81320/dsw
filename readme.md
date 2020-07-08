# create a newsreader with an ML feature

## data acquisition

So far I get data from a german and a US newspaper. I get the links with beautiful soup and download the articles with newspaper3k. I dump them as JSON for the meta data and as plain text for the articles text. There is no database. Reference is through filenames: 00001.json for the meta data and 00001.txt for the main text.

at the moment I am not downloading images. However, I kept links to the top image and all images in meta data.

## data cleaning ...

... might have to follow. Some articles I get are plain adverts. Some links (nytimes) are to interactive visualisations. I have a 'type' (with the option 'article') in the meta data that could help here.

Not doing any data cleaning at the moment. Will do only if required by the ML task.

## prepare data for ML task

## ML task: clustering with Kmeans
