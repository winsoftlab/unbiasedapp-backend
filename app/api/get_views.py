from . import api
from app.api import get_routes
from app.api.authentication import auth
from flask import g, url_for


@api.route('/')
def api_home():
    user = g.current_user
    msg = f'Hello {user.username} welcome to unbiased api please read the docs  to get started'
    return {'msg':msg, 'Documentation': url_for('api.documentation', _external=True)}



@api.route('/facebook/')
def get_all_facebook_analysis():
    '''
    API Endpoint to Get all the Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    '''
    return get_routes.get_all_facebook_analysis()

@api.route('/facebook/analysis/<string:post_id>')
def get_single_facebook_analysis(post_id):
    '''
    API Endpoint to Get a single Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    '''
    return get_routes.get_single_facebook_page_post(post_id)
  

@api.route('/amazon/')
@auth.login_required
def get_amazon_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''

    return get_routes.get_amazon_analysis()


@api.route('/instagram/')
@auth.login_required
def get_instagram_analysis():
    '''
    API endpoint to Get all Instagram processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return get_routes.get_instagram_analysis()


@api.route('/twitter/')
@auth.login_required
def get_twitter_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return get_routes.get_twitter_analysis()