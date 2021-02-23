import nltk


tagged_sents = nltk.corpus.brown.tagged_sents()


def chunk(sentence):
    grammar = r"""
    NOUNP: {<DT>?<JJ.*>*<NN.*>+} # Noun phrase
    CLAUSE: {<VB><NOUNP>}    # Verb"""
    parser = nltk.RegexpParser(grammar)
    result = parser.parse(sentence)
    return result


tuples = set([])
for sent in tagged_sents:
    # Get the tree
    tree = chunk(sent)
    # Look for subtrees
    for subtree in tree.subtrees():
        # If a subtree is the CLASUE we defined as VB -> NP,
        if subtree.label() == 'CLAUSE':
            # Add the verb and the first word of the NP that triggered the match
            tuples.add((subtree[0][0], subtree[1][0][0]))


"""
('Draw', 'each')
('make', 'available')
('find', 'meaning')
('buy', 'copybooks')
('make', 'good')
('increase', 'CDC')
('lessen', 'this')
('speed', 'diagnosis')
('avoid', 'suspicion')
('see', 'objects')
('make', 'definite')
('buy', 'meat')
('eat', 'Western')
('limit', 'delays')
('use', 'wood')
('commit', 'suicide')
('bring', 'long')
('sell', 'dozens')
('describe', 'death')
('put', 'life')
"""
