from flask import Blueprint

user_router = Blueprint('user_route', __name__, url_prefix='/api/user')
