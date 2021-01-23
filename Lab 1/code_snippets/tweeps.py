
from nltk.corpus import stopwords
from tweepy import OAuthHandler, API, Cursor
import nltk
consumer_key = "key"
consumer_secret = "secret"
access_token = "token"
access_token_secret = "secret"

# Setup Tweepy | Boilerplate code
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Cursor return the query, with the given amount of tweets |  Cursor(api.method (search|user_timeline), args -> (q[Query|screen_name[Twitter Handle]]))
statuses = Cursor(api.search, q='software', tweet_mode="extended").items(1)

vocab = set([])

for status in statuses:
    # Add every word to the vocab. Update takes an iterable and adds every element to the set :)
    vocab.update(status.full_text.split())


# NTLK needs to download the packages seperatly
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Set difference is the best operator <3
print(stop_words-vocab)
