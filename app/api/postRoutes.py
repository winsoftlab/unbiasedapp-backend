from flask import jsonify, g, request, session
from flask_login import current_user
from app.api.errors import unauthenticated
from app.controllers.Ecommerce.amazon import begin_amazon_search
from app.controllers.Ecommerce.jumia import begin_jumia_search
from app.controllers.Ecommerce.konga import begin_konga_search
from . import api
from app.controllers.facebookController.facebookScraper import search_facebook, scrape_facebook_page

from app.controllers.Ecommerce.htmlparse import html_parser
from ..controllers.twitterController.processTweets import process_tweets
from ..controllers.instagramController.instagramGetCredentials import getCredentials
from ..controllers.instagramController.InstaGraphAPI import InstagramGraphAPI

from app.controllers.facebookController.facebookGraphAPI import( page_posts_id, 
                                                                get_page_access_token, 
                                                                get_page_post_comments,
                                                                get_page_post_comments_reply)
from app.models import (
    FacebookAnalysis, 
    InstagramAnalysis, 
    AmazonAnalysis, 
    TwitterAnalysis)


from app import db



def search_tweet(q, count):
    '''
    API Endpoint with query parameters query string(q) and count of words for searching tweets
        http://localhost:5000/api/v1/search-tweet/{search-query}/count={count}

    Response:
        Object: Dict_str
    '''
    result = process_tweets(q, count)

    new_twitter_analysis = TwitterAnalysis(
        user_id=g.current_user.id,
        search_query=q,
        sentiments= str(result)
    )

    db.session.add(new_twitter_analysis)
    db.session.commit()


    return result


def scrapping_bee_amazon(product_name, product_id, sub_domain):

    review_data = html_parser(product_name, product_id, sub_domain)

    # new_amazon_analysis = AmazonAnalysis(
    #     user_id=g.current_user.id,
    #     product_info= '{}:{}'.format(product_id, product_id),
    #     sentiments= str(review_data)
    # )

    # db.session.add(new_amazon_analysis)
    # db.session.commit()

    return jsonify(review_data)

def selenium_amazon(product_name, product_id):
    result = dict()
    url = f'https://www.amazon.com/{product_name}/product-reviews/{product_id}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    search_result = begin_amazon_search(url)

    for i in range(0, len(search_result)):
        result[i] = search_result[i]

    return jsonify(result)


def selenium_jumia(product_id):

    result = dict()
    url = f'https://www.jumia.com.ng/catalog/productratingsreviews/sku/{product_id}/'

    search_result = begin_jumia_search(url)

    for i in range(0, len(search_result)):
        result[i] = search_result[i]

    return jsonify(result)


def selenium_konga(product_name_code_url):

    url = f'https://www.konga.com/product/{product_name_code_url}'

    search_result = begin_konga_search(url)

    return {'data': search_result}



def facebook_search(q, page_num):

    '''Route for scrapping facebook based on search keyword and page number'''


    result = search_facebook(q, page_num)
    text = [i['text'] for i in result if 'text' in i.keys()]
    
    # # Create an instance of the data and commit to database
    
    # prev = FacebookAnalysis.query.filter_by(search_query=q).first()
    # #This logic here deletes the previous data if a paritcular search query was found
    # if prev:

    #     db.session.delete(prev)
    #     db.session.commit()

    # new_analysis = FacebookAnalysis(user_id=g.current_user.id, search_query=q, sentiments=str(text))

    # db.session.add(new_analysis)
    # db.session.commit()

    return  jsonify(result)



def facebook_page(page_name, page_num):

    result = scrape_facebook_page(page_name, page_num)
    
    return jsonify(result)


def instagram_comments():

    # if not User.fb_access_token:
    #     return unauthenticated('Please log in facebook from home page')

    params = getCredentials()

    # user = User.query.get(g.current_user.id)
    
    params['access_token'] = session['fb_access_token']

    response = InstagramGraphAPI(**params).get_account_info()
    # print('################################################')
    # print(response)
    page_id = response['data'][0]['id']

    params['page_id'] = page_id
    
    session['page_id'] = page_id
    ig_user_id_response = InstagramGraphAPI(**params).get_instagram_account_id()

    # print('###############################################')
    # print(ig_user_id_response)
 
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
    if not hashtag_search_response['data']:
        return {'msg': f'No data found for hashtag {q}'}

    hashtag_search_id = hashtag_search_response['data'][0]['id']

    params['hashtag_id'] = hashtag_search_id

    _type=request.args.get('type')

    if _type not in ['top_media','recent_media']:
        _type = 'recent_media'

    params['type']= _type or 'recent_media'

    hashtag_media_response = InstagramGraphAPI(**params).get_hashtagMedia()

    return hashtag_media_response

def facebook_page_post_comments():
    params = getCredentials()

    params['access_token'] = session['fb_access_token']  #User access token

    params['page_id'] = session['page_id']

    response = get_page_access_token(**params)

    # print('#############################################################')

    # print(response)

    page_access_token = response['access_token'] #Page access token

    params['page_access_token'] = page_access_token


    page_response= page_posts_id(**params)

    # print('#########################################')
    # print(page_response)

    page_post_id  = page_response['posts']['data'][1]['id']

    params['page_post_id'] = page_post_id

    page_post_response = get_page_post_comments(**params)

    # print('#########################################')
    # print(page_response)

    post_comments = page_post_response['data']
    data = dict()
    for i in range(len(post_comments)):
        comment = post_comments[i]['message']

        comment_id = post_comments[i]['id']

        params['comment_id'] = comment_id

        page_post_comment_reply = get_page_post_comments_reply(**params)

        data[i] = {'comment':comment, 'comment_id':comment_id,'replies': page_post_comment_reply}

    return data
