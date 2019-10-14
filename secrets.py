import tweepy

def login():
    consumer_key="XXXXX"
    consumer_secret="XXXXX"
    access_token="XXXXX"
    access_token_secret="XXXXX"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
