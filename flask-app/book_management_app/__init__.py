from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

# __init__ is where we initialize our application and components
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:iStD-So.043-Database@34.72.136.99/testDB'
app.config["MONGO_URI"] = 'mongodb://admin:iStD-So.043-Database@34.72.136.99:27017/test?authSource=admin'
app.config['SECRET_KEY'] = 'isTdSoo43'

db = SQLAlchemy(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from book_management_app import routes
