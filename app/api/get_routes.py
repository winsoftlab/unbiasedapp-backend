from app.controllers.facebookController.facebook_graph_api import (
    get_page_access_token,
    page_posts_id,
)
from app.controllers.instagramController.instagram_get_credentials import getCredentials
from app.controllers.twitterController.process_tweets import process_tweets
from . import api

from flask import g, jsonify
from flask_login import current_user

from app import db
from app.api.errors import page_not_found
from app.models import (
    FacebookAnalysis,
    AmazonAnalysis,
    InstagramAnalysis,
    TwitterAnalysis,
    JumiaAnalysis,
    KongaAnalysis,
    User,
)
import pickle
import json


def get_facebook_pages():
    """_summary_

    Returns:
        _type_: _description_
    """
    user = User.query.get(g.current_user.id)
    fb_page_lists = json.loads(user.fb_page_id)

    return jsonify(fb_page_lists)


def get_posts(page_id):
    """_summary_

    Args:
        page_id (_type_): _description_

    Returns:
        _type_: _description_
    """

    user = User.query.get(g.current_user.id)

    params = getCredentials()

    params["access_token"] = user.fb_access_token  # User access token

    params["page_id"] = page_id

    # print(user.fb_page_id)

    response = get_page_access_token(**params)

    page_access_token = response["access_token"]  # Page access token

    params["page_access_token"] = page_access_token

    page_response = page_posts_id(**params)

    if not page_response.get("posts"):
        return jsonify([])

    list_of_posts = []

    for i in range(len(page_response["posts"]["data"])):
        _ = dict()
        _[page_response["posts"]["data"][i]["id"]] = (
            page_response["posts"]["data"][i]["message"][:20] + "..."
        )
        list_of_posts.append(_)

    return jsonify(list_of_posts)


def get_all_facebook_analysis():
    """_summary_

    Returns:
        _type_: _description_
    """

    # TODO add sorting parameters from the query parameters parsed from the request.args
    facebook_analysis = FacebookAnalysis.query.filter_by(
        user_id=g.current_user.id
    ).all()

    if facebook_analysis != []:
        data = []
        for items in facebook_analysis:
            data.append({items.fb_post_id: json.loads(items.comments)})
        return jsonify(data)

    return page_not_found("No analysis has been made yet")


def get_single_facebook_page_post(post_id):
    """_summary_

    Args:
        post_id (_str_): _description_

    Returns:
        _type_: _description_
    """
    post = FacebookAnalysis.query.filter_by(fb_post_id=post_id).first()

    _comments = json.loads(post.comments)
    # with open('facebook_replies.txt', 'w') as f:
    #     [f.writelines(k) for k in _comments]

    if post:
        # TODO PROCESSING OF COMMENTS GOES HERE
        return jsonify(_comments)
    return page_not_found("Post not found")


def get_all_twitter_analysis():
    tweets = TwitterAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if tweets == []:
        return page_not_found("No analysis has been made yet")
    all_tweets = []
    for tweet in tweets:
        query = tweet.search_query
        _tweet = pickle.loads(tweet.tweets)
        _result = process_tweets(_tweet)
        all_tweets.append({"search query": query, "result": _result})
    return jsonify(all_tweets)


def get_single_twitter_analysis(search_query):
    """_summary_

    Returns:
        _type_: _description_
    """

    # TODO add sorting parameters from the query parameters parsed from the request.args
    tweet = TwitterAnalysis.query.filter_by(search_query=search_query).first()
    if tweet is not None:
        query = tweet.search_query
        tweets = pickle.loads(tweet.tweets)
        result = process_tweets(tweets)
        return {" search query": query, "result": result}
    return page_not_found("No analysis has been made yet")


def get_amazon_analysis():
    """_summary_

    Returns:
        _type_: _description_
    """

    # TODO add sorting parameters from the query parameters parsed from the request.args
    amazon_analysis = AmazonAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if amazon_analysis != []:
        data = []
        for i in range(0, len(amazon_analysis)):
            data.append(
                {
                    "product": amazon_analysis[i].product_name,
                    "reviews": json.loads(amazon_analysis[i].reviews),
                }
            )
        return jsonify(data)

    return page_not_found("No analysis has been made yet")


def get_single_amazon(product_name, product_id):
    """_summary_

    Args:
        product_id (_type_): _description_
        product_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    product = AmazonAnalysis.query.filter_by(
        product_id=product_id, product_name=product_name
    ).first()

    if product is None:
        return page_not_found(
            f"product with product id {product_id} and produc name {product_name} is not found"
        )

    reviews = json.loads(product.reviews)
    # TODO Sentiments are analysed here
    return jsonify(reviews)


def get_instagram_analysis():
    """_summary_

    Returns:
        _type_: _description_
    """

    # TODO add sorting parameters from the query parameters parsed from the request.args
    instagram_analysis = InstagramAnalysis.query.filter_by(
        user_id=g.current_user.id
    ).all()
    if instagram_analysis != []:
        data = []
        for analysis in instagram_analysis:
            data.append({analysis.insta_post_id: json.loads(analysis.comments)})
        return jsonify(data)
    return page_not_found("No analysis has been made yet")


def get_all_jumia():
    """_summary_

    Returns:
        _type_: _description_
    """
    # TODO add sorting parameters from the query parameters parsed from the request.args
    jumia_analysis = JumiaAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if jumia_analysis != []:
        data = []
        for i in range(0, len(jumia_analysis)):
            data.append(
                {
                    "product": jumia_analysis[i].product_id,
                    "reviews": json.loads(jumia_analysis[i].reviews),
                }
            )
        return jsonify(data)
    return page_not_found("No analysis has been made yet")


def get_single_jumia(product_id):
    """_summary_

    Args:
        product_id (_str_): _description_

    Returns:
        _type_: _description_
    """
    product = JumiaAnalysis.query.filter_by(product_id=product_id).first_or_404()

    if product is None:
        return page_not_found(f"No product with product id {product_id}")

    product_review = json.loads(product.reviews)

    # TODO ANALYSIS IS PERFORMED HERE

    return jsonify(product_review)


def get_all_konga():
    """_summary_

    Returns:
        _type_: _description_
    """

    # TODO add sorting parameters from the query parameters parsed from the request.args

    konga_analysis = KongaAnalysis.query.filter_by(user_id=g.current_user.id).all()

    if konga_analysis != []:
        data = []
        for i in range(0, len(konga_analysis)):
            data.append(
                {
                    "product": konga_analysis[i].product_description,
                    "reviews": json.loads(konga_analysis[i].reviews),
                }
            )
        return jsonify(data)
    return page_not_found("No analysis has been made yet")


def get_single_konga(product_description):
    product = KongaAnalysis.query.filter_by(
        product_description=product_description
    ).first()
    if product is None:
        return page_not_found(
            f"product with description {product_description} not found"
        )
    reviews = json.loads(product.reviews)

    # TODO Sentiments is analysed here

    return jsonify(reviews)
