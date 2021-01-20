from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from tweepy import OAuthHandler, API, Cursor
import nltk
import json


consumer_key = "lE2ZjoYIMcgyF8CuUWDc9DT5c"
consumer_secret = "0Y3eRg3cPh12dUVdPpcCLwIz0DTN9Cjialqew2PylNcqGo7RGq"
access_token = "1304419499807051776-oRMqjKalvLOVIYtHJXFVO4RbiNMbr6"
access_token_secret = "pOJFu54jrRxUyya15NQGLldzPUZwbqxtUTPfdeCDZJxnW"
# Setup Tweepy | Boilerplate code
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)
twitter_timeline = api.home_timeline()
terms = ['anime', 'artificial intelligence', 'nlp', 'backend', 'frontend', 'database',
         'language technology', 'music', 'nodejs', 'python', 'running', 'training', 'Suits', 'software']
# Cursor return the query, with the given amount of tweets |  Cursor(api.method (search|user_timeline), args)
for term in terms:
    statuses = Cursor(api.search, q=term, tweet_mode="extended").items(250)
    with open(f"tweets/terms/{term}.json", 'w+') as file:
        file.write(json.dumps([status._json for status in statuses]))
