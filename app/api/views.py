from flask import jsonify, g, redirect, request, session, url_for
from .authentication import auth
from app.api.errors import unauthenticated
from . import api
from app.controllers.facebookController.facebook import scrape_facebook_post
from app.controllers.others.htmlparse import html_parser
from ..controllers.twitterController.processTweets import process_tweets
from ..controllers.instagramController.instagramGetCredentials import getCredentials
from ..controllers.instagramController.InstaGraphAPI import InstagramGraphAPI


@api.route('/')
def api_home():
    user = g.current_user
    msg = f'Hello {user.username} welcome to unbiased api please read the docs  to get started'
    return {'msg':msg}

@api.route('/search-tweet', methods=['POST'])
def search_tweet():
    '''
    API Endpoint with query parameters query string(q) and count of words for searching tweets
        http://localhost:5000/api/v1/search-tweet?q={search-query}&count={count}

    Response:
        Object: Dict_str
    '''
    q = request.args.get('q')
    count= int(request.args.get('count'))


    result = process_tweets(q, count)

    return result


@api.route('/amazon', methods=['GET'])
def scrapping_bee_amazon():

    '''
    API endpoint with query parameters product-name:str, product-id:str, sub_domain(default='com')

    http://localhost:5000/api/v1/amazon?product-name={product-name}&product-id={product-id}&sub-domain={sub-domain}
    
    '''
    product_name:str = request.args.get('product_name')
    product_id:str = request.args.get('product_id')
    sub_domain= request.args.get('sub_domain') or 'com'

    review_data = html_parser(product_name, product_id, sub_domain)

    return jsonify(review_data)



@api.route('/facebook', methods=['GET'])
def scrapping_bee_facebook():
    '''
    API Endpoint with query parameters query string(q) and page_num for
        searching facebook data.
        http://localhost:5000/api/v1/facebook?q={query-string}&page-num={page-num}

    '''
    q= request.args.get('q')
    page_num= int(request.args.get('page_num'))

    result = scrape_facebook_post(q, page_num)

    return jsonify(result)

@api.route('/instagram/token', methods=['POST'])
def get_access_token():
    '''
    Get access code and store it in session
    '''

    access_token = request.form.get('access_token')
    session['short_access_token'] = access_token
    return redirect(url_for('api.debug_access_token'))
    #return{'msg':"access code retrieved succesfully"}


@api.route('/instagram/debug-token')
def debug_access_token():
    '''
        Debug access token and reassign
    '''
    access_token = session['short_access_token']

    params = getCredentials()

    params['access_token'] = access_token

    response =InstagramGraphAPI(**params).debug_long_lived_token()

    session['fb_access_token'] = response['access_token']

    return {'short':session['short_access_token'],'long':session['fb_access_token']}
       



@api.route('/instagram/get-account-info')
def get_account_info():

    if not session['fb_access_token']:
        return unauthenticated('Please log in to facebook')

    params = getCredentials()
    params['access_token'] = session['fb_access_token']
    response = InstagramGraphAPI(**params).get_account_info()
    page_id = response['data'][0]['id']
    session['page_id'] = page_id

    return {'page_id':page_id}


@api.route('/instagram/hashtag-search/<string:q>', methods=['GET'])
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





@api.route('/instagram/comments', methods=['GET'])
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


    
@api.route('/instagram/process-comments')
def process_instagram_comments():
    comments= request.form.get('')
    return{'msg':'process comment'}
