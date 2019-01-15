"""
This module defines all the user endpoints
"""

import uuid
import datetime
from flask import request, jsonify, make_response

# local imports
from app.api.v1.utils.meetup_validators import MeetupValidator
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup import Meetup

v1 = Blueprint('meetupv1', __name__, url_prefix='/api/v1/')

meetup_models = Meetup('meetup_db')

""" This route performs a get request to fetch all upcoming meetups """
@v1.route("/meetups/upcoming", methods=['GET'])
def get_all_meetups():
    meetups = meetup_models.get_items()

    return make_response(jsonify({
        "status": 200,
        "meetups": meetups
    }), 200)

""" This route posts a meetup """
@v1.route("/meetups/", methods=['POST'])
def post_a_meetup():
    data = request.get_json()

    # Validate meetup
    validate_meetup = MeetupValidator(
        data['topic'],
        data['description'],
        data['tags'],
        data['happeningOn'],
        data['location']
    )

    meetups = meetup_models.get_items()

    meetup = {
        "topic": data['topic'],
        "description": data['description'],
        "location": data['location'],
        "happeningOn": data['happeningOn'],
        "tags": data['tags'],
        "id": len(meetups), # str(uuid.uuid4()),
    }

    def errorHandler(error):
        return make_response(jsonify({
            "error": error
        }), 422) 
    
    if validate_meetup.data_exists():
        return errorHandler(validate_meetup.data_exists())
    elif validate_meetup.valid_topic():
        return errorHandler(validate_meetup.valid_topic())
    elif validate_meetup.valid_description():
        return errorHandler(validate_meetup.valid_description())
    elif validate_meetup.valid_tags():
        return errorHandler(validate_meetup.valid_tags())
    elif validate_meetup.valid_date():
        return errorHandler(validate_meetup.valid_date())
    elif validate_meetup.valid_location():
        return errorHandler(validate_meetup.valid_location())
    elif meetup_models.save_meetup(meetup) == 'No data found':
        return make_response(jsonify({
            "error": 'No data found'
        }), 404)
    else:
        return make_response(jsonify({
            "status": 201,
            "message": "You have successfully posted a meetup",
            "data": [{
                "topic": data['topic'],
                "location": data['location'],
                "happeningOn": data['happeningOn'],
                "tags": data['tags'],
            }],
        }), 201)

""" This route fetches a specific meetup """
@v1.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    meetup = meetup_models.get_item_by_id(meetupId)

    if meetup:
        return jsonify({
            "status": 200,
            "data": meetup
        }), 200
    else:
        return make_response(jsonify({
            "error": 'Meetup not found!'
        }), 404)
        
""" This route posts RSVPS on meetups """
@v1.route("/meetups/<int:meetupId>/rsvp", methods=['POST'])
def post_RSVP(meetupId):
    data = request.get_json()
    meetups = meetup_models.get_items()
    meetup = [meetup for meetup in meetups if meetup['id'] == meetupId]

    if meetup:
        
        topic = meetup[0]['topic'].upper()

        rsvp = {
            "meetup": meetupId,
            "topic": topic,
            "status": data['status']
        }

        def confirm():
            if rsvp['status'] == "yes":
                return "You have successfully RSVP'd on {} meetup".format(topic)
            elif rsvp['status'] == "no":
                return "You have confirmed you're not attending the {} meetup".format(topic)
            elif rsvp['status'] == "maybe":
                return "You have confirmed you might attend the {} meetup".format(topic)
            else:
                return make_response(jsonify({
                    "error": 'type: YES, NO, MAYBE to RSVP'
                }), 404)

            meetup_models.rsvp_meetup(meetupId, topic)
                    
        return jsonify({
            "status": 200,
            "message": confirm(),
            "data": rsvp
        }), 201
    else:
        return make_response(jsonify({
            "error": 'Meetup not found or doesn\'nt exist'
        }), 404)
