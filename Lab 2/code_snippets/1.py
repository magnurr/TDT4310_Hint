import nltk
from collections import defaultdict

# Get the bible from the gutenberg collection
bible_txt = nltk.corpus.gutenberg.words('bible-kjv.txt')
# Tag the words
tagged_bible_txt = nltk.pos_tag(bible_txt)
# Default dictonary gives every new entry a default value, it is a set in this case.
dicts = defaultdict(lambda: set([]))
# Add all tags for the words to the dictonary
for word, tag in tagged_bible_txt:
    dicts[word].add(tag)

# Sorting if your into that :)
sorted_dict = dict(sorted(dicts.items(),
                          key=lambda item: len(item[1])))

print(sorted_dict)
