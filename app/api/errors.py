

from app.exceptions import ValidationError
from flask import request, jsonify, render_template
from . import api
from ..main import main


@main.app_errorhandler(404) #----probably problematic
def page_not_found(e='Not found'):
    if request.accept_mimetypes.accept_json:
        response = jsonify({'error':e})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500) #----probably problematic
def internal_server_error(e=None):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Internal Server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500


def forbiden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

def unauthenticated(message):
    response = jsonify({'error':"unauthenticated",'message':message})
    response.status_code = 401
    return response

@api.errorhandler(ValidationError)
def validation_error(e):
    pass #bad_request(e.args[0])
