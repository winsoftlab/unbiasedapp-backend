from . import api
from app import db
from app.models import FacebookAnalysis, AmazonAnalysis, InstagramAnalysis,TwitterAnalysis
from flask_login import current_user


def get_all_facebook_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    facebook_analysis = FacebookAnalysis.query.filter_by(user_id=current_user.id).all()
    return {'Data': facebook_analysis}

def get_twitter_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    twitter_analysis =TwitterAnalysis.query.filter_by(user_id=current_user.id).all()
    return{'Data': twitter_analysis}

def get_amazon_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    amazon_analysis = AmazonAnalysis.query.filter_by(user_id=current_user.id).all()
    return{'Data': amazon_analysis}

def get_instagram_analysis():

    #TODO add sorting parameters from the query parameters parsed from the request.args
    instagram_analysis=InstagramAnalysis.query.filter_by(user_id=current_user.id).all()
    return{'Data':instagram_analysis}