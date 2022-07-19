from flask_login import login_required, session_protected
from itsdangerous import json
from ..controllers.twitterController.processTweets import processTweets
from . import data
from flask_cors import cross_origin
from flask import jsonify, request, url_for
from ..decorators import subscription_required




def before_request():
    pass

@data.route('/get_tweets', methods=["POST"])
@login_required
@cross_origin()
def get_tweets():
    query = request.form.get('query')
    count = 100 #request.args['count']
    result= processTweets(query, count)

    return result