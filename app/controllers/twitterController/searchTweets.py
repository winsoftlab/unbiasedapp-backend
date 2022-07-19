from .connectTwitter import connect_api
import tweepy as tw

twitterApi = connect_api()

def search_tweets(search_query, count):

    from_date = "2020-09-16"

    tweets = tw.Cursor(
        twitterApi.search_tweets,
        q=search_query,
        lang="en",
        since=from_date
        ).items(count)

    return tweets