from flaskblog.app import create_app

#app.config.from_object('__init__')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
