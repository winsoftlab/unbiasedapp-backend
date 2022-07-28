import os
import tweepy as tw
from config import Config

def connect_api():
    
    auth = tw.OAuthHandler(os.getenv('TWITTER_KEY'), os.getenv('TWITTER_SECRET'))

    twitterApi = tw.API(auth, wait_on_rate_limit=True)

    return twitterApi

