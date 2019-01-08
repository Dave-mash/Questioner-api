[![Build Status](https://travis-ci.org/Dave-mash/Questioner-api.svg?branch=develop)](https://travis-ci.org/Dave-mash/Questioner-api)
# Questioner-api application endpoints
## The following are API endpoints enabling one to:
* Create an account and log in.
* Create a meetup record.
* Fetch a meetup record.
* Get all meetup records.
* Get meetup questions.
* Post a question on a meetup.
* Comment to a meetup question.
* Edit a question
* Delete a question
* Edit a meetup
* Delete a meetup
* View comments
* RSVP for a meeting
* Upvote or Downvote a question
### Prerequisites
* Python3
* Git
* Postman
### Questioner application endpoints
| Endpoint        | Functionality           | HTTP method  |
| ------------- |:-------------:| -----:|
| `/auth/signup`      | Register a user | POST |
| `/auth/login`      | Login a user       |   POST |
| `/meetup` | Post a meetup       |    POST |
| `/meetup/<meetup-id>` | Fetch a meetup       |    GET |
| `/meetups/upcoming` | Fetch all meetups       |    GET |
| `/questions` | Post a question       |    POST |
| `/questions/<questionId>` | Delete a question        |    DELETE |
| `/questions/<questionId>/comment` | Post a comment to a  question        |    POST |
| `/questions/<questionId>/upvote` | Increase votes by 1        |    PATCH |
| `/questions/<questionId>/downvote` | Decrease votes by 1        |    PATCH |
| `/meetups/<meetup-id>/rsvps` | Respond to meetup RSVP        |    POST |

### Authors
David Macharia @[Dave-mash](https://github.com/Dave-mash)
