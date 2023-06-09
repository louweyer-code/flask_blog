from flask_login import LoginManager
from flaskblog.users.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))