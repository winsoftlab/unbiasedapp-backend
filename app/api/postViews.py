
from flask import g,url_for, session
from app.api import postRoutes
from . import api
from app import auto
from app.api.authentication import auth


@auto.doc()
@api.route('/search-tweet/<string:q>/<int:count>', methods=['POST'])
def search_tweet(q, count=100):
    return postRoutes.search_tweet(q, count)

@auto.doc()
@api.route('/amazon/<string:product_name>/<string:product_id>', methods=['POST','GET'])
def amazon_search(product_name, product_id):

    return postRoutes.selenium_amazon(product_name, product_id)


@auto.doc()
@api.route('/amazon/<string:product_name>/<string:product_id>/<string:sub_domain>', methods=['POST','GET'])
def scrapping_bee_amazon(product_name, product_id, sub_domain='com'):

    '''
    API endpoint with query parameters product-name:str, product-id:str, sub_domain(default='com')

    http://localhost:5000/api/v1/amazon/{product-name}/{product-id}/{sub-domain}
    
    '''
    return postRoutes.scrapping_bee_amazon(product_name, product_id, sub_domain)


@auto.doc()
@api.route('/jumia/<string:product_id>', methods=['POST','GET'])
def jumia_search(product_id):

    return postRoutes.selenium_jumia(product_id)

@auto.doc()
@api.route('/konga/<string:product_name_code_url>', methods=['POST','GET'])
def konga_search(product_name_code_url):

    return postRoutes.selenium_konga(product_name_code_url)

@auto.doc()
@api.route('/facebook/search/<string:q>/<int:page_num>', methods=['POST','PUT', 'GET'])
def facebook_search(q, page_num=2):
    '''
    API Endpoint with query parameters query string(q) and page_num for
        searching facebook data.
        http://localhost:5000/api/v1/facebook/{query-string}/{page-num}

    '''
    return postRoutes.facebook_search(q, page_num)

@auto.doc()
@api.route('/facebook/posts/<string:page_name>/<int:page_num>', methods=['POST','PUT', 'GET'])
def facebook_page(page_name='bbcnews', page_num=2):
    '''
    API Endpoint with query parameters query string(q) and page_num for
        searching facebook data.
        http://localhost:5000/api/v1/facebook/posts/{facebook-page}/{page-num}

    '''
    return postRoutes.scrape_facebook_page(page_name, page_num)

@auto.doc()
@api.route('/instagram/hashtag-search/<string:q>', methods=['POST','GET'])
def instagram_hashtag(q):
    return postRoutes.instagram_hashtag(q)


@auto.doc()
@api.route('/facebook/page-post-comments')
def facebook_page_post():
    return postRoutes.facebook_page_post_comments()


@auto.doc()
@api.route('/instagram/comments', methods=['GET'])
def instagram_comments():
    return postRoutes.instagram_comments()

