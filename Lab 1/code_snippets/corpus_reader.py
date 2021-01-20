import nltk
import matplotlib.pyplot as plt


# FileIds are found by nltk.corpus.[corpus_name].fileids(), this is the names of the files within the corpus
fileids = nltk.corpus.brown.fileids()
output = {}
for ID in fileids:
    # Getting a given document can be done as following : nltk.corpus.[corpus_name].[split_type](fileids=[ID])
    sentences = nltk.corpus.brown.sents(fileids=ID)
    average_length = sum([len(sent) for sent in sentences])/len(sentences)
    output[ID] = average_length

# Equal length lists to represent the values in x and y directions
x_axis = list(output.keys())
y_axis = list(output.values())

# using a bar graph, you can use .plot to get points or lines if applicable
plt.bar(x_axis, y_axis)
#Rotating labels so they don't overlap :)
plt.xticks(rotation=90)

# Show the graph
plt.show()
