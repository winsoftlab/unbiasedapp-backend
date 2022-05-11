from . import demo
from flask import request, render_template
from flask_cors import cross_origin
from ..tasks import gettweets_pipeline, analyise_tweet_pipe

@demo.route('/dashboard', methods=["GET"])
def demo_dashboard():
    return render_template('demo/demo.html')

@demo.route('/demo-tweets', methods=["POST"])
@cross_origin()
def demo_tweets():
    """
    """
    if request.method == "POST":

        search_query = request.form.get("query")

        item_data_count = 100
        
        tweets = gettweets_pipeline(search_query, item_data_count)

        result = analyise_tweet_pipe(tweets)

        
        return result