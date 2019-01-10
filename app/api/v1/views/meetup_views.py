"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response
from app.api.v1.models.meetup_model import MeetupModel
from .. import version1 as v1

meetup_model = MeetupModel()

@v1.route("/meetups/", methods=['GET'])
def get():
    return make_response(jsonify({
        "users": meetup_model.db
    }), 200)
