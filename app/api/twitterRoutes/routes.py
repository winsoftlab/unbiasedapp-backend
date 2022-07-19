from flask import jsonify
from .. import api
from ...controllers.twitterController.searchTweets import search_tweets

@api.route('/twitter/<str:query>/<int:count>', methods=['POST'])
def search_tweets(query, count):
    search_results = search_tweets(query, count)

    return jsonify(search_results)