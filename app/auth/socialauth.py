from . import auth
from app import oauth, db
import os
from flask import url_for, redirect


@auth.route('/facebook/')
def facebook_login():
    # Facebook Oauth Config
    FACEBOOK_CLIENT_ID = os.environ.get('FACEBOOK_APP_ID')
    FACEBOOK_CLIENT_SECRET = os.environ.get('FACEBOOK_APP_SECRET')
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/v14.0',
        client_kwargs={'scope': 'email business_management user_posts instagram_basic'},
    )
    redirect_uri = url_for('auth.facebook_auth', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)

@auth.route('/authorize/facebook/')
def facebook_auth():
    token = oauth.facebook.authorize_access_token()
    resp =oauth.facebook.get(
        'https://graph.facebook.com/v14.0/me?fields=id,name,email,picture{url}'
    )
    profile = resp.json()
    #TODO: Save the user to the database and the access_token
    print('Facebook User', profile)
    return redirect('/')


@auth.route('/twitter/')
def twitter_login():
    TWITTER_CLIENT_ID = os.environ.get('TWITTER_KEY')
    TWITTER_CLIENT_SECRET = os.environ.get('TWITTER_SECRET')
    oauth.register(
        name='twitter',
        client_id=TWITTER_CLIENT_ID,
        client_secret=TWITTER_CLIENT_SECRET,
        request_token_url='https://api.twitter.com/oauth/request_token',
        request_token_params=None,
        access_token_url='https://api.twitter.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://api.twitter.com/oauth/authenticate',
        authorize_params=None,
        api_base_url='https://api.twitter.com/2/',
        client_kwargs=None,
    )
    redirect_uri = url_for('auth.twitter_auth', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)

@auth.route('/authorize/twitter/')
def twitter_auth():
    token = oauth.twitter.authorize_access_token()
    resp = oauth.twitter.get('account/verify_credentials.json')
    profile = resp.json()
    print(" Twitter User", profile)
    return redirect('/')
  
