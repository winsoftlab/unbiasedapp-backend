from flask import render_template, render_template_string
from . import main
from authlib.integrations.flask_client import OAuthError


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


@main.app_errorhandler(401)
def unauthorized(e):
    return render_template("errors/401.html"), 401


@main.app_errorhandler(OAuthError)
def oauth_error(e):
    return render_template_string(
        f"<html><body><h1>Oauth Error</h1><p>Error {e} occured during authentication</p></body></html>"
    )
