import tweepy
import time
from tweepy import Cursor
import json


def return_unq(jsonFile):
    return {each['id']: each for each in jsonFile}.values()


def write_only_unq(path):
    with open(path, "r+") as file:
        obj = file.read()
        obj = json.loads(obj)
        obj = return_unq(obj)
        json.dump(list(obj), file)


TWITTER_API_KEY = "lE2ZjoYIMcgyF8CuUWDc9DT5c"
TWITTER_API_SECRET = "0Y3eRg3cPh12dUVdPpcCLwIz0DTN9Cjialqew2PylNcqGo7RGq"
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFdMKwEAAAAA0eg%2BK%2FHAg55JnOft%2Fd6UuhlTiuE%3Dg8jdWFBhYlhJBW8AbQh2gb3vrlAMRc0hMWBDhsqldBUo4mn7qc"
TWITTER_ACCESS_TOKEN_KEY = "1304419499807051776-PIqrjagIK26DWcBCnbDY2hLFkADILd"
TWITTER_ACCESS_TOKEN_SECRET = "gYrj8BnmiLxDccRtrJx50zGRmE4padYPZ1bdxDoERVz7L"


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

users = ["jaden", "MileyCyrus"]


def main():
    total_tweet_count = 0
    for user in users:
        tweets = []
        last_50_id = []
        tweets_per_qry = 100
        since_id = None
        max_id = -1
        max_tweets = 3100
        tweet_count = 0
        while tweet_count < max_tweets:
            print('start')
            try:
                if max_id <= 0:
                    if not since_id:
                        new_tweets = Cursor(api.user_timeline, screen_name=user, lang="en", include_rts=True,
                                            tweet_mode='extended').items(3100)
                if not new_tweets:
                    print("No more tweets found")
                    break
                listNewTweets = [tweet._json for tweet in new_tweets]
                tweets.extend(listNewTweets)
                tweet_count += len(listNewTweets)
                print(user)
                print(max_id)
                if listNewTweets:
                    lastTweet = listNewTweets[-1]
                    max_id = lastTweet.get('id')
                if len(last_50_id) < 50:
                    last_50_id.append(max_id)
                else:
                    last_50_id.pop(0)
                    last_50_id.append(max_id)
                if (len(last_50_id) == 50 and all(elem == max_id for elem in last_50_id)):
                    break

            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
        output = {}
        output[user] = tweets
        total_tweet_count += tweet_count
        with open(f'../tweets/users/{user}.json', "w") as file:
            json.dump(output[user], file)
    print("Downloaded at least {0} tweets, Saved to csv file".format(
        total_tweet_count))


main()