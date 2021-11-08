from flask import Blueprint

main = Blueprint('main', __name__)

from core.main import views