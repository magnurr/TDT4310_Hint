import nltk
from sklearn.model_selection import train_test_split
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger

tagged_brown_sents = nltk.corpus.brown.tagged_sents()

brown_50_test, brown_50_train = train_test_split(
    tagged_brown_sents, test_size=0.5)


default = DefaultTagger("NN")  # Should use most common tag in data set :/
uni = UnigramTagger(train=brown_50_train, backoff=default)
bi = BigramTagger(train=brown_50_train, backoff=uni)
tri = TrigramTagger(train=brown_50_train, backoff=uni)

default_acc = default.evaluate(brown_50_test)
uni_acc = uni.evaluate(brown_50_test)
bi_acc = bi.evaluate(brown_50_test)
tri_acc = tri.evaluate(brown_50_test)

print("Accuracy for Brown \n==============================")
print("Default Tagger:", default_acc)
print("Unigram (backoff=DefaultTagger):", uni_acc)
print("Bigram Tagger (backoff=Unigram):", bi_acc)
print("Trigram Tagger (backoff=Bigram):", tri_acc)

"""
Accuracy for Brown 
==============================
Default Tagger: 0.13085226235223996
Unigram (backoff=DefaultTagger): 0.8945585028130825
Bigram Tagger (backoff=Unigram): 0.9133009016334138
Trigram Tagger (backoff=Bigram): 0.9080554416694516
"""
