from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import csv
from nltk import stem
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from sklearn.model_selection import train_test_split

stemmer = stem.PorterStemmer()
content = []

with open('spam.csv', newline='', encoding='latin-1') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        content.append(row)
texts = [row[1] for row in content]
labels = [row[0] for row in content]
stopwords = set(stopwords.words('english'))


def encode_labels(ls):
    # Ternary operator + list comprehension, horrible to read, easy to write :/
    return [1 if ls == "ham" else 0 for label in ls]


def text_cleaning(text):
    text = text.lower()
    text = " ".join([word for word in word_tokenize(text)
                     if not word in stopwords])
    text = re.sub(r"[!?:;-,.<>]", r"", text)
    text = " ".join([stemmer.stem(word) for word in text])
    return text

#apply functions to dataset 
map(text_cleaning, texts)
map(encode_labels, labels)

# split it 
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.1, random_state=420)

# Vectorize :slurp: 
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
# OMG I AM MACHINE LEARNING! 
svm = svm.SVC(C=1000)
svm.fit(X_train, y_train)
# Evaluate performacnce
X_test = vectorizer.transform(X_test)
y_pred = svm.predict(X_test)

#Percision and recall 
print(confusion_matrix(y_test, y_pred))
