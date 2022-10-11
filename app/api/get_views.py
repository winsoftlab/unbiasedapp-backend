from . import api
from app.api import get_routes
from flask import g, url_for


@api.route("/")
def api_home():
    user = g.current_user
    msg = f"Hello {user.username} welcome to unbiased api please read the docs  to get started"
    return {"msg": msg, "Documentation": url_for("api.documentation", _external=True)}


@api.route("/get-facebook-pages")
def show_pages():
    return get_routes.get_facebook_pages()


@api.route("/show-page-posts/<string:page_id>")
def show_post(page_id):
    return get_routes.get_posts(page_id)


@api.route("/instagram/")
def get_instagram_analysis():
    """
    API endpoint to Get all Instagram processed data
    Can take query parameters, like date sorting , most recent, and by query string
    """
    return get_routes.get_instagram_analysis()


@api.route("/twitter/")
def get_twitter_analysis():
    """
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    """
    return get_routes.get_twitter_analysis()


@api.route("/facebook/")
def get_all_facebook_analysis():
    """
    API Endpoint to Get all the Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    """
    return get_routes.get_all_facebook_analysis()


@api.route("/facebook/analysis/<string:post_id>")
def get_single_facebook_analysis(post_id):
    """
    API Endpoint to Get a single Facebook analysis by a user
    Can take query parameters, like date sorting , most recent, and by query string

    """
    return get_routes.get_single_facebook_page_post(post_id)


# ---------ECOMMMERCE VIEWS-----------


@api.route("/amazon/")
def get_amazon_analysis():
    """
    API endpoint to Get all Amazon processed data
    Can take query parameters, like date sorting , most recent, and by query string
    """

    return get_routes.get_amazon_analysis()


@api.route("/amazon/<string:product_id>/<string:product_name>")
def get_single_amazon_analysis(product_id, product_name):
    """_summary_

    Args:
        product_id (_type_): _description_
        product_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    return get_routes.get_single_amazon(product_id, product_name)


@api.route("/konga/")
def get_konga_analysis():
    """_summary_

    Returns:
        _type_: _description_
    """
    return get_routes.get_all_konga()


@api.route("/konga/<string:product_description>")
def get_single_konga_analysis(product_description):
    """_summary_

    Args:
        product_description (_type_): _description_

    Returns:
        _type_: _description_
    """
    return get_routes.get_single_konga(product_description)


@api.route("/jumia/")
def get_all_jumia_analysis():
    """_summary_

    Returns:
        _type_: _description_
    """
    return get_routes.get_all_jumia()


@api.route("/jumia/<string:product_id>")
def get_single_jumia_analysis(product_id):
    """_summary_

    Args:
        product_id (_type_): _description_
    """

    return get_routes.get_single_jumia(product_id)
