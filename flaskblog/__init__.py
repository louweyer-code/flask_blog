import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flaskblog import routes
from dotenv import load_dotenv
 
load_dotenv()

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    #postgresql://database_blog_za4j_user:eY02HhqhqzBt2U8FsveENlSqWTQdH5Bg@dpg-cgq7bvgrddlaefdp8370-a.frankfurt-postgres.render.com/database_blog_za4j
    db.init_app(app)

    return app



#db = SQLAlchemy()
#app = Flask(__name__)
#app.config['SECRET_KEY'] = '1234'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# #db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
#db.init_app(app)

#from flaskblog import routes

#with app.app_context():
#    db.create_all()
