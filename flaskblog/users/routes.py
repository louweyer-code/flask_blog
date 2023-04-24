from flask import render_template, url_for, flash, redirect, request, Blueprint, current_app
from flaskblog.extensions.database import db
# from .forms import RegistrationForm, LoginForm
from flaskblog.users.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

#from flaskblog.app import bcrypt

blueprint = Blueprint('blog', __name__)

#home with posts
@blueprint.route("/")
@blueprint.route("/home")
def posts():
    page_number = request.args.get('page', 1, type=int)
    posts = Post.query.all()
    posts_pagination = Post.query.paginate(page=page_number, per_page=current_app.config['POSTS_PER_PAGE'])
    return render_template('posts.html', posts_pagination=posts_pagination)


#register routes
@blueprint.get('/register')
def get_register():
  return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
  try:
    if request.form.get('password') != request.form.get('password_confirmation'):
      raise Exception('The password confirmation must match the password.')
    elif User.query.filter_by(email=request.form.get('email')).first():
      raise Exception('The email address is already registered.')

    user = User(
      email=request.form.get('email'),
      password=generate_password_hash(request.form.get('password'))
    )
    user.save()

    return 'User created'
  except Exception as error_message:
    error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
    return render_template('users/register.html', error=error)



#about
@blueprint.route("/about")
def about():
    return render_template('about.html', title='About')


#new post
@blueprint.get('/new')
def get_newpost():
  return render_template('new.html', posts=posts)

@blueprint.post('/new')
def post_newpost():
  posts = Post.query.all()

  post = Post(
    slug='placeholder slug',
    title=request.form.get('title'),
    content=request.form.get('content'),
    user_id=current_user.get_id()
  )

  if not all([
    request.form.get('title'),
    request.form.get('content'),
  ]):
    return render_template('new.html', posts=posts, error='Please fill out all fields.')

  post.save()
  return redirect('/')


#login
@blueprint.get('/login')
def get_login():
  return render_template('users/login.html', title='Login')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()
    
    if not user:
      raise Exception('No user with the given email address was found.')
    elif not check_password_hash(user.password, request.form.get('password')):
       raise Exception('The password does not appear to be correct.')

    login_user(user)
    return redirect('/home')
    
  except Exception as error_message:
    error = error_message or 'An error occurred while logging in. Please verify your email and password.'
    return render_template('users/login.html', error=error)
  
@blueprint.get('/logout')
def logout():
  logout_user()

  return redirect('/home')



# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]


# @blueprint.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data, password=generate_password_hash)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('users/register.html', title='Register', form=form)


# @blueprint.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('users/login.html', title='Login', form=form)

# @blueprint.get('/logout')
# def logout():
#   return 'User logged out'
