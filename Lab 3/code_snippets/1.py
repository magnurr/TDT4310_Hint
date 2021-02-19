from random_word import RandomWords
import random
from sklearn.model_selection import train_test_split
import nltk
r = RandomWords()


def generate_dataset():
    output = []
    for x in range(10):
        label = random.randint(0, 1)
        text = r.get_random_words(
            minLength=3, maxLength=15, limit=random.randint(5, 15))
        if not text:
            continue
        output.append(tuple([text, label]))
    return output


def generate_features(text):
    return {"last-word": text[-1], "Amount-of-words": len(text), "Length of text": len(" ".join(text))}


labeled_features = generate_dataset()
featuresets = [(generate_features(text), label)
               for (text, label) in labeled_features]

print("Training :)")
train_set, test_set = featuresets[5:], featuresets[:5]

dt_classifier = nltk.DecisionTreeClassifier.train(train_set)
nb_classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(dt_classifier, test_set))
print(nltk.classify.accuracy(nb_classifier, test_set))
