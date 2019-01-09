from flask import Flask
from .api.v1.views.user_views import version1 as user_v1    

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_v1)

    return app
