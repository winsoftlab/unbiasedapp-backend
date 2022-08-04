from flask import jsonify, g, request
from . import api
from app.controllers.facebookController.facebook import scrape_facebook_post
from app.controllers.others.htmlparse import html_parser
from . import api
from ..controllers.twitterController.processTweets import process_tweets


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
    q:str = request.args.get('q')
    count= int(request.args.get('count'))


    result = process_tweets(q, count)

    return result


@api.route('/amazon', methods=['POST'])
def scrapping_bee_amazon():

    '''
    API endpoint with query parameters product-name:str, product-id:str, sub_domain(default='com')

    http://localhost:500/api/v1/amazon?product-name={product-name}&product-id={product-id}&sub-domain={sub-domain}
    
    '''
    product_name:str = request.args.get('product_name')
    product_id:str = request.args.get('product_id')
    sub_domain= request.args.get('sub_domain') or 'com'

    review_data = html_parser(product_name, product_id, sub_domain)

    return jsonify(review_data)



@api.route('/facebook', methods=['POST'])
def scrapping_bee_facebook():
    '''
    API Endpoint with query parameters query string(q) and page_num for
        searching facebook data.
        http://localhost:5000/api/v1/facebook?q={query-string}&page-num={page-num}

    '''
    q= request.args.get('q')
    page_num= int(request.args.get('page_num'))

    #result = scrape_facebook_post(q, page_num)

    return{'q':q, 'page_num':page_num} #jsonify(result)

@api.route('/instagram/hashtag-search', methods=['POST'])
def instagram_hashtag():
    return {'instagram'}
