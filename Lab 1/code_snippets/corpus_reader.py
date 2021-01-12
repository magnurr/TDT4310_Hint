import nltk
from collections import Counter
import matplotlib.pyplot as plt
import random
# FileIds are found by nltk.corpus.[corupus_name].fileids()
fileids = nltk.corpus.state_union.fileids()
# Getting a given document can be done as following : nltk.corpus.[corpus_name].words(fileids=[ID])
words = nltk.corpus.state_union.words(fileids=fileids[0])
# returns an object that has the count of each word
obj = Counter(words)
# Getting the 10 most common words
obj.most_common(10)

# Plot the words to a graph
plt.plot([random.randint(0, 40)
          for x in range(20)], [random.randint(0, 40)
                                for y in range(20)], 'ro')
plt.xticks(rotation=90)
plt.show()
