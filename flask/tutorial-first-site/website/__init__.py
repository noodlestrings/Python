# for settting up flask app
# calling the file init.py makes the folder a python package so other files can access this method directly from import
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkeyforapp'

    #imnporting blueprints
    from .views import views
    from .auth import auth

    #defining url prefix to the defined .route decorator
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
