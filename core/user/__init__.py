from flask import Blueprint

user = Blueprint('user',__name__)

from core.user import views
