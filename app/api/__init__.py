from flask import Blueprint

api = Blueprint('api',__name__)

from . import errors, authentication, decorators, getRoutes, getViews, postRoutes, postViews