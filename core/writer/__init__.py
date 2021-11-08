from flask import Blueprint

writer = Blueprint('writer',__name__)

from core.writer import views