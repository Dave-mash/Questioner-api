from flask import Flask
from .api.v1.views.user_views import v1 as user_v1    
from .api.v1.views.meetup_views import v1 as meetup_v1    
from .api.v1.views.question_views import v1 as question_v1    
from config import app_config

def create_app(config_name="development"):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config["development"])
    app.register_blueprint(user_v1)
    app.register_blueprint(meetup_v1)
    app.register_blueprint(question_v1)

    return app
