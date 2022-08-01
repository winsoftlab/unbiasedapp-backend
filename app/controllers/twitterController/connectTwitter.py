import os
import tweepy as tw
from config import Config

def connect_api():
    auth = tw.OAuthHandler(os.environ.get('TWITTER_KEY'), os.environ.get('TWITTER_SECRET'))

    twitterApi = tw.API(auth, wait_on_rate_limit=True)

    return twitterApi