"""
This module defines all the user endpoints
"""

import uuid
import datetime
from flask import request, jsonify, make_response

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel

v1 = Blueprint('meetupv1', __name__, url_prefix='/api/v1/')

meetup_model = MeetupModel()

""" This route performs a get request to fetch all meetups """
@v1.route("/meetups/", methods=['GET'])
def get_all_meetups():
    return make_response(jsonify({
        "meetups": meetup_model.db
    }), 200)


@v1.route("/meetups/", methods=['POST'])
def post_a_meetup():
    data = request.get_json()
    # datetime.datetime.now()
    meetup = {
        "id": "{}".format(uuid.uuid4()),
        "location": data['location'],
        "topic": data['topic'],
        "happeningOn": data['happeningOn']
        # "tags": data['tags']
    }

    if meetup_model.write_meetup(meetup):
        return jsonify({
            "status": 422,
            "Error": "Please make your topic unique."
        })
    else:
        return jsonify({
            "status": 201,
            "message": "You have successfully posted a meetup",
            "data": [{
                "location": data['location'],
                "topic": data['topic'],
                "happeningOn": data['happeningOn']
                # "tags": data['tags']
            }]
        }), 201