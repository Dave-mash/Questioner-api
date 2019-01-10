from flask import Flask
from .api.v1.views.user_views import v1 as user_v1    
from .api.v1.views.meetup_views import v1 as meetup_v1    

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_v1)
    app.register_blueprint(meetup_v1)

    return app
