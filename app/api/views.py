from flask import jsonify, g,request
from . import api
from ..controllers.twitterController.searchTweets import search_tweets
from app.controllers.facebookController.facebook import scrape_facebook_post
from app.controllers.others.htmlparse import html_parser
from . import api
from ..controllers.twitterController.processTweets import process_tweets


@api.route('/')
def api_home():
    user = g.current_user
    msg = f'Hello {user.username} flask api works'
    return {'msg':msg}

@api.route('/search-tweet', methods=['POST'])
def search_tweet():
    data= request.get_json()
    query = data['query']
    count = data['count']
    result = process_tweets(query, count)

    return result


@api.route('/others/amazon', methods=['POST'])
def scrapping_bee_amazon():

    data= request.get_json()

    product_name = data['product_name']

    product_id = data['product_id']

    sub_domain = data['sub_domain']
    
    review_data = html_parser(product_name, product_id, sub_domain)


    return jsonify(review_data)



@api.route('/others/facebook', methods=['POST'])
def scrapping_bee_facebook():
    data = request.get_json()
    query = data['query']
    page_num=data['page_num']
    result = scrape_facebook_post(query, page_num)
    return jsonify(result)

    