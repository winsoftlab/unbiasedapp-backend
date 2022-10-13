from . import api
from flask import jsonify, g, request, session
from flask_login import current_user
from app.api.errors import unauthenticated
from app.controllers.Ecommerce.amazon import begin_amazon_search
from app.controllers.Ecommerce.jumia import begin_jumia_search
from app.controllers.Ecommerce.konga import begin_konga_search
from app.controllers.twitterController.search_tweets import search_tweets
from ..controllers.instagramController.instagram_get_credentials import getCredentials
from ..controllers.instagramController.Insta_graph_api import InstagramGraphAPI
from app.controllers.facebookController.facebook_graph_api import (
    get_page_access_token,
    get_page_post_comments,
    get_page_post_comments_reply,
)
from app.models import (
    FacebookAnalysis,
    InstagramAnalysis,
    AmazonAnalysis,
    TwitterAnalysis,
    JumiaAnalysis,
    KongaAnalysis,
    User,
)


from app import db
import pickle
import json


def search_tweet(q, count):
    """
    API Endpoint with query parameters query string(q) and count of words for searching tweets
        http://localhost:5000/api/v1/search-tweet/{search-query}/count={count}

    Response:
        Object: Dict_str
    """
    result = search_tweets(q, count)

    _tweet = pickle.dumps(result)

    analysis = TwitterAnalysis.query.filter_by(search_query=q).first()

    if analysis is None:
        new_twitter_analysis = TwitterAnalysis(
            user_id=g.current_user.id, search_query=q, tweets=_tweet
        )
        db.session.add(new_twitter_analysis)
    else:
        analysis.tweets = _tweet
    db.session.commit()
    return {"msg": "Data retrieved successfully"}


def selenium_amazon(product_name, product_id):
    # result = dict()
    url = f"https://www.amazon.com/{product_name}/product-reviews/{product_id}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent"

    # cm_cr_dp_d_show_all_btm?

    search_result = begin_amazon_search(url)
    _search_result = json.dumps(search_result)

    product = AmazonAnalysis.query.filter_by(
        user_id=g.current_user.id, product_id=product_id
    ).first()

    if product is None:
        new_search = AmazonAnalysis(
            user_id=g.current_user.id,
            product_id=product_id,
            product_name=product_name,
            reviews=_search_result,
        )

        db.session.add(new_search)
    else:

        product.reviews = _search_result

    db.session.commit()

    # for i in range(0, len(search_result)):
    #     result[i] = search_result[i]

    return {"msg": "Data retrieved successfully"}


def selenium_jumia(product_id):

    result = dict()
    url = f"https://www.jumia.com.ng/catalog/productratingsreviews/sku/{product_id}/"

    search_result = begin_jumia_search(url)
    _search_result = json.dumps(search_result)

    product = JumiaAnalysis.query.filter_by(product_id=product_id).first()

    if product is None:
        new_search = JumiaAnalysis(
            user_id=g.current_user.id, product_id=product_id, reviews=_search_result
        )

        db.session.add(new_search)
    else:

        product.reviews = _search_result
    db.session.commit()

    for i in range(0, len(search_result)):
        result[i] = search_result[i]

    return jsonify(result)


def selenium_konga(product_name_code_url):

    url = f"https://www.konga.com/product/{product_name_code_url}"

    search_result = begin_konga_search(url)
    _search_result = json.dumps(search_result)

    product_description = KongaAnalysis.query.filter_by(
        product_description=product_name_code_url
    ).first()

    if product_description is None:
        new_search = KongaAnalysis(
            user_id=g.current_user.id,
            product_description=product_name_code_url,
            reviews=_search_result,
        )
        db.session.add(new_search)
    else:
        product_description.reviews = _search_result
    db.session.commit()

    return {"msg": "Data retrieved successfully"}


def instagram_comments():

    user = User.query.get(g.current_user.id)

    if user is None or user.fb_access_token is None:
        return unauthenticated("Please Login facebook to access api")

    params = getCredentials()

    params["access_token"] = user.fb_access_token

    # FB PAGE ID IS A LIST of dictionaries
    _p_id = None
    for key in json.loads(user.fb_page_id)[1].keys():
        _p_id = key
        print(_p_id)

    params["page_id"] = _p_id

    # params["page_id"] = json.loads(user.fb_page_id)[
    #     0
    # ].keys()  # I am accessing the first one with the key S

    ig_user_id_response = InstagramGraphAPI(**params).get_instagram_account_id()

    print(ig_user_id_response)

    ig_user_id = ig_user_id_response["instagram_business_account"]["id"]

    params["instagram_account_id"] = ig_user_id

    ig_user_media_response = InstagramGraphAPI(**params).get_user_media()
    ig_user_media_id = ig_user_media_response[0]["data"][0]["id"]

    params["ig_media_id"] = ig_user_media_id

    media_response = InstagramGraphAPI(**params).getComments()

    ig_comment_and_reply_list = []  # A list of IG Comments and replies as a single unit

    for i in media_response["data"]:
        ig_comment_and_reply_list.append(i["text"])
        if i.get("replies") != None:
            for j in i["replies"]["data"]:
                ig_comment_and_reply_list.append(j["text"])

    analysis = InstagramAnalysis.query.filter_by(insta_post_id=ig_user_media_id).first()
    _ig_comment_and_reply_list = json.dumps(ig_comment_and_reply_list)

    # SAVING TO DATABASE
    if analysis is None:
        new_analysis = InstagramAnalysis(
            user_id=g.current_user.id,
            insta_post_id=ig_user_media_id,
            comments=_ig_comment_and_reply_list,
        )

        db.session.add(new_analysis)
    else:
        analysis.comments = _ig_comment_and_reply_list

    db.session.commit()

    return {"msg": "Data successfully retrieved"}


def instagram_hashtag(q):

    user = User.query.get(g.current_user.id)

    if user is None and user.fb_access_token is None:
        return unauthenticated("Please Login facebook to access api")

    params = getCredentials()

    params["access_token"] = session["fb_access_token"]
    params["access_token"] = user.fb_access_token
    params["page_id"] = user.fb_page_id

    ig_user_id_response = InstagramGraphAPI(**params).get_instagram_account_id()

    ig_user_id = ig_user_id_response["instagram_business_account"]["id"]
    params["instagram_account_id"] = ig_user_id
    params["hashtag_name"] = q

    hashtag_search_response = InstagramGraphAPI(**params).get_hashtagsInfo()
    key = "data"
    if key not in hashtag_search_response.keys():
        return {"msg": f"No data found for hashtag {q}"}

    hashtag_search_id = hashtag_search_response["data"][0]["id"]

    params["hashtag_id"] = hashtag_search_id

    _type = request.args.get("type")

    if _type not in ["top_media", "recent_media"]:
        _type = "recent_media"

    params["type"] = _type or "recent_media"

    hashtag_media_response = InstagramGraphAPI(**params).get_hashtagMedia()

    return hashtag_media_response


def retrieve_posts_id(page_response):
    """A function that returns the post id from the page response"""

    post_id = page_response["posts"]["data"][1]["id"]

    # for i in range(len(posts)):
    #     yield posts[i]["id"]
    return post_id


# def show_facebook_pages(user):
#     fb_pages = user.fb_page_id
#     return fb_pages

# def list_facebook_posts_id(fb_page_d):

#     return list_of_posts_id


def facebook_page_post_comments(page_id, post_id):
    """A function that gets the comments from a particular facebook
    post using the page id and the page access token
    """

    user = User.query.get(g.current_user.id)

    if user is None or user.fb_access_token is None:
        return unauthenticated("Please login with Facebook to access facebook data")

    params = getCredentials()

    params["access_token"] = user.fb_access_token  # User access token

    params["page_id"] = page_id

    response = get_page_access_token(**params)

    page_access_token = response["access_token"]  # Page access token

    params["page_access_token"] = page_access_token

    params["page_post_id"] = post_id

    page_post_response = get_page_post_comments(**params)

    post_comments = page_post_response["data"]

    comment_reply_list = (
        []
    )  # Empty list of comment and replies as a single list content

    for i in range(len(post_comments)):
        comment = post_comments[i]["message"]

        comment_reply_list.append(comment)  # adding comment to list

        comment_id = post_comments[i]["id"]

        params["comment_id"] = comment_id

        page_post_comment_reply = get_page_post_comments_reply(**params)

        if (
            page_post_comment_reply["data"] != []
        ):  # checking if data exit i.e The comment has a reply
            for j in range(len(page_post_comment_reply["data"])):
                comment_reply_list.append(page_post_comment_reply["data"][j]["message"])

    analysis = FacebookAnalysis.query.filter_by(fb_post_id=post_id).first()
    _comment_reply_list = json.dumps(comment_reply_list)

    if analysis is None:
        new_analysis = FacebookAnalysis(
            user_id=g.current_user.id,
            fb_page_id=page_id,
            fb_post_id=post_id,
            comments=_comment_reply_list,
        )

        db.session.add(new_analysis)
    else:
        analysis.comments = _comment_reply_list

    db.session.commit()

    return {"msg": "Data successfully retrieved"}
