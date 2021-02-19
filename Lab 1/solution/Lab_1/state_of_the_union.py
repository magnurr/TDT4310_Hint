import nltk
from nltk.corpus import state_union

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    # For each file
    for fileid in state_union.fileids()
    # Find all the words
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people']
    # filter out so we only return words in target
    if w.lower() == target)
cfd.plot()


""" The most interesting things to note that i saw was the spike in use of the word people by Bill Clinton, and how there was a spike in the use of the word men around the end of the second world war.
Something that no one noted was the intersting dip in the use of all words the year after JFK was killed. There might be a joke about conspiracy theories hidden somewhere in here :smirk:"""
