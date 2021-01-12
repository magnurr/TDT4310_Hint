
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import time
import sys
from tweepy import OAuthHandler, API, Cursor
import nltk


consumer_key = "lE2ZjoYIMcgyF8CuUWDc9DT5c"
consumer_secret = "0Y3eRg3cPh12dUVdPpcCLwIz0DTN9Cjialqew2PylNcqGo7RGq"
access_token = "1304419499807051776-oRMqjKalvLOVIYtHJXFVO4RbiNMbr6"
access_token_secret = "pOJFu54jrRxUyya15NQGLldzPUZwbqxtUTPfdeCDZJxnW"
# Setup Tweepy | Boilerplate code
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)
twitter_timeline = api.home_timeline()

# Cursor return the query, with the given amount of tweets
statuses = Cursor(api.search, q='software').items(100)
for status in statuses:
    pass


# Most common words in english that will not impart any meaning to a text
stop_words = set(stopwords.words('english'))
# How to use a tokenizer made for Twitter, (special syntax rules)
tt = TweetTokenizer()
tt.tokenize('string')
