from flask import g,url_for
from app.api import postRoutes
from app.api.errors import forbiden
from . import api
from app import auto
from app.api.authentication import auth

@api.route('/')
def api_home():

    user = g.current_user
    msg = f'Hello {user.username} welcome to unbiased api please read the docs  to get started'
    return {'msg':msg, 'Documentation': url_for('api.documentation')}



@api.route('/documentation')
def documentation():

    '''The endpoint for the Auto documentation of the API 
        http://localhost:5000/api/v1/documentation
     '''
    return auto.html()



@auto.doc()
@api.route('/search-tweet/<string:q>/<int:count>', methods=['POST'])
def search_tweet(q, count=100):
    return postRoutes.search_tweet(q, count)


@auto.doc()
@api.route('/amazon/<string:product_name>/<string:product_id>/<string:sub_domain>', methods=['POST'])
def scrapping_bee_amazon(product_name, product_id, sub_domain='com'):

    '''
    API endpoint with query parameters product-name:str, product-id:str, sub_domain(default='com')

    http://localhost:5000/api/v1/amazon/{product-name}/{product-id}/{sub-domain}
    
    '''
    return postRoutes.scrapping_bee_amazon(product_name, product_id, sub_domain)


@auto.doc()
@api.route('/facebook/<string:q>/<int:page_num>', methods=['POST','PUT'])
def facebook(q, page_num=2):
    '''
    API Endpoint with query parameters query string(q) and page_num for
        searching facebook data.
        http://localhost:5000/api/v1/facebook/{query-string}/{page-num}

    '''
    return postRoutes.facebook(q, page_num)


@auto.doc()
@api.route('/instagram/hashtag-search/<string:q>', methods=['POST'])
def instagram_hashtag(q):
    return postRoutes.instagram_hashtag(q)


@auto.doc()
@api.route('/instagram/comments', methods=['POST'])
def instagram_comments():
    return postRoutes.instagram_comments()

