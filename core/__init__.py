from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask

# from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:next23rd@localhost/mtcflask'
# should be hidden in environment variable
app.config['SECRET_KEY'] = 'lc\xf6\xa5\x90LJ\x17=68\x9eK\x9dtM?%\x8b\xb8\xb0cvo'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
# mysql = MySQL(app)

from app.main import main
from app.users import users

app.register_blueprint(main)
app.register_blueprint(users)