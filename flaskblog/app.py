from flask import Flask
from flaskblog.extensions.database import db, migrate
from flaskblog.users.routes import blueprint as bp_users
from flaskblog.extensions.authentication import login_manager
#from flaskblog.users import users, simple_pages, posts
#from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskblog.config')
    #postgresql://database_blog_za4j_user:eY02HhqhqzBt2U8FsveENlSqWTQdH5Bg@dpg-cgq7bvgrddlaefdp8370-a.frankfurt-postgres.render.com/database_blog_za4j
    register_extensions(app)
    register_blueprints(app)
    #bcrypt = Bcrypt(app)

    return app

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)
  login_manager.init_app(app)

def register_blueprints(app: Flask):
  #app.register_blueprint(bp_users)
  app.register_blueprint(bp_users)
  # app.register_blueprint(simple_pages.routes.blueprint)
  # app.register_blueprint(posts.routes.blueprint)
