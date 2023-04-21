from flaskblog.app import create_app
from flaskblog.users.models import User, Post
from flaskblog.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

posts_data = {
  '1':{
      'title':'Post Title Entry 1 test', 
      'content':'Post content entry 1 test',
      'user_id':1
    },

  '2':{
      'title':'Post Title Entry 2 test', 
      'content':'Post content entry 2 test',
      'user_id':2
    },
}

users_data = {
  1:{
      'email':'userone@gmail.com',
      'password':'test',
      'image':'https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png',
    },

  2:{
      'email':'usertwo@gmail.com',
      'password':'test',
      'image':'https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png',
    },
}

for slug, post in posts_data.items():
    new_post = Post(slug=slug, title=post['title'], content=post['content'], user_id=post['user_id'])
    db.session.add(new_post)

for id, user in users_data.items():
    new_user = User(id=id, email=user['email'], password=user['password'], image=user['image'])
    db.session.add(new_user)

db.session.commit()
