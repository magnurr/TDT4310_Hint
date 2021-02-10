import json
import os
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from collections import Counter
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from tweepy import OAuthHandler, API, Cursor
import nltk


consumer_key = "fzztxLfMxj5YGH0vHoDaHOxxw"
consumer_secret = "BNmZ4JDvcBq5InxKk07mynfreo54UBgRwMrl76MHkwzIrwtPv4"
access_token = "1304419499807051776-6VuCZmdcYCOLJbDB03eRddQbEm0SGq"
access_token_secret = "viORwlItvp9VMVga9C2LgaEOVMkzNRGSRgMikb0Pa4C8N"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)
twitter_timeline = api.home_timeline()
terms = ['anime', 'artificial intelligence', 'nlp', 'backend', 'frontend', 'database',
         'language technology', 'music', 'nodejs', 'python', 'running', 'training', 'Suits', 'software']

stop_words = set(stopwords.words('english'))
tt = TweetTokenizer()
user_terms = defaultdict(lambda: [])
corpus = []

# getting data from Twitter
for term in terms:
    statuses = Cursor(api.search, q=term, include_rts=False,
                      tweet_mode="extended").items(10)
    for status in statuses:
        user_terms[term].append(status.full_text)
        corpus.append(status.full_text)

# Storing data
with open('data/full_dump.txt', 'w+') as filepath:
    filepath.writelines(corpus)

for term in user_terms:
    with open(f'data/{term}.txt', 'w+') as filepath:
        filepath.writelines(user_terms[term])

# Transform from raw text to tokens
word_corpus = []
word_user_terms = defaultdict(lambda: [])
for term in user_terms:
    for text in user_terms[term]:
        cleaned_words = [word for word in tt.tokenize(
            text) if not word.lower() in stop_words]
        word_corpus.extend(cleaned_words)
        word_user_terms[term].extend(cleaned_words)

# most common word in corpora
# A little note here, the most common words will probably be gibberish, unless you filter out things like  and other symboles.
corpusCounter = Counter(word_corpus)
print(f"{corpusCounter.most_common(10)} are the most common words in the dataset.")

# most common word in each corpus
for key in user_terms:
    tempCo = Counter(word_user_terms[key])
    print(
        f"The term : {key} has the following most common terms: {tempCo.most_common(10)}")

# most common hashtag in corpora
hashtags = filter(lambda x: x.startswith("#"), word_corpus)
hashtagsCounter = Counter(hashtags)
print(f"{hashtagsCounter.most_common(10)} are the most common hashtags in the dataset.")
