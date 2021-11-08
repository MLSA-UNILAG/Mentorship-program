from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# should be hidden in environment variable
app.config['SECRET_KEY'] = 'lc\xf6\xa5\x90LJ\x17=68\x9eK\x9dtM?%\x8b\xb8\xb0cvo'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from core.main import main
from core.user import user
from core.writer import writer

app.register_blueprint(main)
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(writer,url_prefix='/writer')
