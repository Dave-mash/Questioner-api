"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel
# from .. import version1 as v1
v1 = Blueprint('meetupv1', __name__, url_prefix='/api/v1/')

meetup_model = MeetupModel()

@v1.route("/meetups/", methods=['GET'])
def get():
    return make_response(jsonify({
        "meetups": meetup_model.db
    }), 200)
