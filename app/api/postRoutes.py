from flask import jsonify, g, request, session
from flask_login import current_user
from app.api.errors import unauthenticated
from . import api
from app.controllers.facebookController.facebook import scrape_facebook_post
from app.controllers.others.htmlparse import html_parser
from ..controllers.twitterController.processTweets import process_tweets
from ..controllers.instagramController.instagramGetCredentials import getCredentials
from ..controllers.instagramController.InstaGraphAPI import InstagramGraphAPI
from app.models import FacebookAnalysis, InstagramAnalysis, AmazonAnalysis, TwitterAnalysis
from app import db



def search_tweet(q, count):
    '''
    API Endpoint with query parameters query string(q) and count of words for searching tweets
        http://localhost:5000/api/v1/search-tweet/{search-query}/count={count}

    Response:
        Object: Dict_str
    '''
    q = request.args.get('q')
    count= int(request.args.get('count'))
    result = process_tweets(q, count)

    new_twitter_analysis = TwitterAnalysis(
        user_id=current_user.id,
        query=q,
        sentiment= str(result)
    )

    db.session.add(new_twitter_analysis)
    db.session.commit()


    return result


def scrapping_bee_amazon(product_name, product_id, sub_domain):

    review_data = html_parser(product_name, product_id, sub_domain)

    new_amazon_analysis = AmazonAnalysis(
        user_id=current_user.id,
        product_info= '{}:{}'.format(product_id, product_id),
        sentiment= str(review_data)
    )

    db.session.add(new_amazon_analysis)
    db.session.commit()

    return jsonify(review_data)



def facebook(q, page_num):

    '''Route for scrapping facebook based on search keyword and page number'''


    result = scrape_facebook_post(q, page_num)
    text = [i['text'] for i in result if 'text' in i.keys()]
    
    # Create an instance of the data and commit to database
    new_analysis = FacebookAnalysis(user_id=current_user.id, query=q, sentiment=str(text))

    db.session.add(new_analysis)
    db.session.commit()

    return  jsonify(text)


def instagram_comments():

    if not session['fb_access_token']:
        return unauthenticated('Please log in facebook')

    params = getCredentials()

    params['access_token'] = session['fb_access_token']

    params['page_id'] = session['page_id']

    ig_user_id_response = InstagramGraphAPI(**params).get_instagram_account_id()
 
    ig_user_id = ig_user_id_response['instagram_business_account']['id']

    params['instagram_account_id'] = ig_user_id


    ig_user_media_response = InstagramGraphAPI(**params).get_user_media()
    ig_user_media_id = ig_user_media_response[0]['data'][0]['id']

    params['ig_media_id'] = ig_user_media_id

    media_response = InstagramGraphAPI(**params).getComments()

    return{'media_response': media_response}



def instagram_hashtag(q):
    if not session['fb_access_token']:
        return unauthenticated('Please log in facebook')

    params = getCredentials()

    params['access_token'] = session['fb_access_token']
    params['page_id'] = session['page_id']
    ig_user_id_response = InstagramGraphAPI(**params).get_instagram_account_id()
 
    ig_user_id = ig_user_id_response['instagram_business_account']['id']
    params['instagram_account_id'] = ig_user_id
    params['hashtag_name'] = q

    hashtag_search_response = InstagramGraphAPI(**params).get_hashtagsInfo()
    hashtag_search_id = hashtag_search_response['data'][0]['id']

    params['hashtag_id'] = hashtag_search_id

    _type=request.args.get('type')

    if _type not in ['top_media','recent_media']:
        _type = 'recent_media'

    params['type']= _type or 'recent_media'

    hashtag_media_response = InstagramGraphAPI(**params).get_hashtagMedia()

    return hashtag_media_response
