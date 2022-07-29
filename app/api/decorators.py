'''
from functools import wraps
from flask import g, request, redirect, url_for
from flask_login import current_user
from .errors return unauthenticated

def authenticate_with_token(f):
    """
    A decorator function that checks for authentication headers
    in requests
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.get.header['Authorization'].split(" ")

        if auth_header[0] == 'Bearer':
            if auth_header[1]: #check if the bearer token is expired here
                pass #pass for now
        else :
            return unaunthenticated('Invalid credentials')
        return f(*args, **kwargs)
    return decorated_function
'''
