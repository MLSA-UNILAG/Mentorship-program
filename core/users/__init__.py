from flask import Blueprint

users = Blueprint('users',__name__)

from core.users import routes
