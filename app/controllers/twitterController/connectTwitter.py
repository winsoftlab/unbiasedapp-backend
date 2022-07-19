import tweepy as tw
from config import Config


def connect_api():
    auth = tw.OAuthHandler(Config.TWITTER_KEY, Config.TWITTER_SECRET)

    twitterApi = tw.API(auth, wait_on_rate_limit=True)

    return twitterApi

