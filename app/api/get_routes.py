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
    )



def get_all_facebook_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    facebook_analysis = FacebookAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if facebook_analysis !=[]:
        data = dict()
        for items in facebook_analysis:
            data[items.search_query] = items.sentiments
            #return {'Key Word':items.search_query, 'Data': items.sentiments}
        return data
    
    return page_not_found('No analysis has been made yet')

def get_twitter_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    twitter_analysis =TwitterAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if  twitter_analysis  !=[]:
        data = dict()
        for i in range(0, len(twitter_analysis)):
            data[i] =  {'query':twitter_analysis[i].search_query, 'sentiment': twitter_analysis[i].sentiments}
        return data

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