#app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
 
load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
db.init_app(app)

from flaskblog import routes

with app.app_context():
    db.create_all()
