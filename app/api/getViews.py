from . import api
from app import auto
from app.api import getRoutes
from app.api.authentication import auth
from flask import g, url_for


@api.route('/')
def api_home():

    user = g.current_user
    msg = f'Hello {user.username} welcome to unbiased api please read the docs  to get started'
    return {'msg':msg, 'Documentation': url_for('api.documentation', _external=True)}



@api.route('/documentation')
def documentation():

    '''The endpoint for the Auto documentation of the API 
        http://localhost:5000/api/v1/documentation
     '''
    return auto.html()


@api.route('/facebook/', methods=['GET'])
@auto.doc()
def get_all_facebook_analysis():
    '''
    API Endpoint to Get all the Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    '''
    return getRoutes.get_all_facebook_analysis()
  



@auto.doc()
@api.route('/amazon')
@auth.login_required
def get_amazon_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''

    return getRoutes.get_amazon_analysis()




@auto.doc()
@api.route('/instagram')
@auth.login_required
def get_instagram_analysis():
    '''
    API endpoint to Get all Instagram processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return getRoutes.get_instagram_analysis()

@auto.doc()
@api.route('/twitter')
@auth.login_required
def get_twitter_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return getRoutes.get_twitter_analysis()