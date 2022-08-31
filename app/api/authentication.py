from os import access
from flask_httpauth import HTTPBasicAuth
from app import db
from ..models import User
from flask import g, jsonify, session, redirect, url_for, request
from .errors import unauthenticated, forbiden
from . import api
from ..controllers.instagramController.instagramGetCredentials import getCredentials
from ..controllers.instagramController.InstaGraphAPI import InstagramGraphAPI


auth = HTTPBasicAuth()

@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbiden('Unconfirmed account')


@api.route('/token/', methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthenticated('Invalid credentials')
        
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600) ,'expiration':3600})

@auth.verify_password
def verify_password(email_or_token, password):
    if email_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None

    user = User.query.filter_by(email=email_or_token).first()

    if not user:
        return False

    g.current_user = user
    g.token_used = False

    return user.verify_password(password)


@api.route('/instagram/token', methods=['POST','PUT'])
def get_access_token():
    '''
    Get access code and store it in session
    '''
    # user = User.query.filter_by(email=g.current_user.email).first()

    # if not user:
    #     return False

    # g.current_user = user

    access_token = request.form.get('access_token')
    params = getCredentials()
    params['access_token'] = access_token
    session['short_access_token'] = access_token

    response = InstagramGraphAPI(**params).debug_long_lived_token()
    session['fb_access_token'] = response['access_token']
    # response =InstagramGraphAPI(**params).debug_long_lived_token()

    # new_token=User(fb_access_token=response['access_token'])
    # db.session.add(new_token)
    # db.session.commit()

    return{'msg':"access code retrieved succesfully"}

@auth.error_handler
def auth_error():
    return unauthenticated('Invalid credentials')