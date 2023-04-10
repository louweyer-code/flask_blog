#app.py
from flaskblog import app

#app.config.from_object('__init__')

if __name__ == '__main__':
    app.run(debug=True)