import os
from flask import Flask
from flaskblog.extensions.database import db
from flaskblog.routes import blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    #postgresql://database_blog_za4j_user:eY02HhqhqzBt2U8FsveENlSqWTQdH5Bg@dpg-cgq7bvgrddlaefdp8370-a.frankfurt-postgres.render.com/database_blog_za4j
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
  db.init_app(app)

def register_blueprints(app: Flask):
   app.register_blueprint(blueprint)