from . import api
from app import auto
from app.api import getRoutes
from app.api.authentication import auth


@api.route('/facebook/', methods=['GET'])
@auto.doc()
def get_all_facebook_analysis():
    '''
    API Endpoint to Get all the Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    '''
    return getRoutes.get_all_facebook_analysis()
  


@auth.login_required
@auto.doc()
@api.route('/amazon')
def get_amazon_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''

    return getRoutes.get_amazon_analysis()



@auth.login_required
@auto.doc()
@api.route('/instagram')
def get_instagram_analysis():
    '''
    API endpoint to Get all Instagram processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return getRoutes.get_instagram_analysis()



@auth.login_required
@auto.doc()
@api.route('/twitter')
def get_twitter_analysis():
    '''
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    '''
    return getRoutes.get_twitter_analysis()