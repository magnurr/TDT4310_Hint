
from nltk.corpus import stopwords
from tweepy import OAuthHandler, API, Cursor
import nltk
# Yes, you can borrow my login details, but if to many people do it, they might turn of the keys or throttle the connections.
consumer_key = "lE2ZjoYIMcgyF8CuUWDc9DT5c"
consumer_secret = "0Y3eRg3cPh12dUVdPpcCLwIz0DTN9Cjialqew2PylNcqGo7RGq"
access_token = "1304419499807051776-oRMqjKalvLOVIYtHJXFVO4RbiNMbr6"
access_token_secret = "pOJFu54jrRxUyya15NQGLldzPUZwbqxtUTPfdeCDZJxnW"

# Setup Tweepy | Boilerplate code
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Cursor return the query, with the given amount of tweets |  Cursor(api.method (search|user_timeline), args -> (q[Query|screen_name[Twitter Handle]]))
statuses = Cursor(api.search, q='software', tweet_mode="extended").items(250)

texts = []
for status in statuses:
    """
    dict_keys(['created_at', 'id', 'id_str', 'full_text', 'truncated', 'display_text_range', 'entities', 'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id',
              'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'retweeted_status', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'lang'])
    """
    texts.append(status._json['full_text'])

#NTLK needs to download the packages seperatly
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
the_cool_words = []


for stop_word in stop_words:
    presence = False
    for sent in texts:
        if stop_word in sent:
            presence = True
    if not (presence):
        the_cool_words.append(stop_word)

print(the_cool_words)
