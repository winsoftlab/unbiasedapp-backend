from app.controllers.twitterController.process_tweets import process_tweets
from . import api

from flask import g
from flask_login import current_user

from app import db
from app.api.errors import page_not_found
from app.models import (
    FacebookAnalysis, 
    AmazonAnalysis, 
    InstagramAnalysis,
    TwitterAnalysis,
    JumiaAnalysis,
    KongaAnalysis
    )
import pickle
import json

def get_all_facebook_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    facebook_analysis = FacebookAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if facebook_analysis !=[]:
        data = dict()
        for items in facebook_analysis:
            data[items.search_query] = items.sentiments
        return data
    
    return page_not_found('No analysis has been made yet')


def get_single_facebook_page_post(post_id):
    post = FacebookAnalysis.query.filter_by(fb_post_id=post_id).first()

    _comments = json.loads(post.comments)
    # with open('facebook_replies.txt', 'w') as f:
    #     [f.writelines(k) for k in _comments]

    if post:
        #TODO PROCESSING OF COMMENTS GOES HERE
        return{'data':_comments}
    return page_not_found('Post not found')


def get_twitter_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    tweet =TwitterAnalysis.query.filter_by(user_id=g.current_user.id).first()
    
    #twitter_analysis =TwitterAnalysis.query.filter_by(user_id=g.current_user.id).all()
    # if  twitter_analysis  !=[]:
    #     # data = dict()
    #     # for i in range(0, len(twitter_analysis)):
    #     #     data[i] =  {'query':twitter_analysis[i].search_query, 'sentiment': twitter_analysis[i].sentiments}
    #     # return data
    if tweet:
        query = tweet.search_query
        tweets = pickle.loads(tweet.tweets)
        result = process_tweets(tweets)
        return {' search query': query, 'result': result}
    return page_not_found('No analysis has been made yet')


def get_amazon_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    amazon_analysis = AmazonAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if  amazon_analysis !=[]:
        data = dict()
        for i in range(0, len(amazon_analysis)):
            data[i] =  {'query':amazon_analysis[i].product_info, 'sentiment': amazon_analysis[i].sentiments}
        return data
    
    return page_not_found('No analysis has been made yet')


def get_instagram_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    instagram_analysis=InstagramAnalysis.query.filter_by(user_id=g.current_user.id).all()
    if instagram_analysis !=[]:
        return {'Data':instagram_analysis}
    
    return page_not_found('No analysis has been made yet')