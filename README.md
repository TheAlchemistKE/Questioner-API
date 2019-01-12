[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0dd5d80a20f94c2da86808f0c20125fd)](https://app.codacy.com/app/KelynPNjeri/Questioner-API?utm_source=github.com&utm_medium=referral&utm_content=KelynPNjeri/Questioner-API&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/KelynPNjeri/Questioner-API.svg?branch=develop)](https://travis-ci.com/KelynPNjeri/Questioner-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/ff91486e5e85335922eb/maintainability)](https://codeclimate.com/github/KelynPNjeri/Questioner-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/KelynPNjeri/Questioner-API/badge.svg?branch=develop)](https://coveralls.io/github/KelynPNjeri/Questioner-API?branch=develop)
# Questioner API(Version 1)
Questioner web app, is an online platform that crowd-sources questions from users about meetups.

## API ENDPOINTS
To run the endpoints in postman:
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/470df32a30646e961eb9)
#### Question Endpoints.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/questions  | Create a question for a specific meetup  | POST  |
| /api/v1/questions  | Get all questions for a specific meetup  | GET  |
| /api/v1/questions/question-id | Get a specific question  | GET  |
| /api/v1//questions/question-id/upvote  | Upvote a specific question.  | PATCH  |
|/api/v1/questions/question-id/downvote  | Downvote a specific question. | PATCH |

#### Meetup Endpoints
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/meetups  | Get all meetups  | GET  |
| /api/v1/meetups  | Create a meetup  | POST  |
|/api/v1/meetups/meetup-id | Get a specific meetup record  | GET  |
|/api/v1/meetups/meetup-id/rsvps  | Respond to meetup RSVP  | POST  |

## Getting Started
To get started:
1. Git clone the repository using `git clone https://github.com/KelynPNjeri/Questioner-API.git`

### Prerequisites
For the API to run smoothly tou will need the following:
```
1. Python 3.6 or higher installed.
2. Pip3
3. Pipenv or virtualenv installed.
```
### Installing
> __Installation Guide.__

1. Git clone the repository using `git clone https://github.com/KelynPNjeri/Questioner-API.git`.
2. Through your terminal, navigate to the location with the cloned repository.
3. Open the cloned repo folder using your terminal.
4. You're currently on the `develop` branch.
5. Set up a virtual environment:
    > Using virtualenv: `virtualenv -p python3 env`
    > Using pipenv: `pipenv shell`
6. To activate the virtual environment:
    > Using virtualenv: `source env/bin/activate`
    > Using pipenv: `not necessary`(since it automatically activates itself after creation)
7. Install the packages:
    > Using virtualenv: `pip3 install -r requirements.txt`
    > Using pipenv: `pipenv install`
8. There is already a `.env` file containing all the necessary environment variables.
9. Export all the environment variables by running `source .env`.
10. To launch your app now, use `flask run`.

## Running the tests
To view all the unit tests, from your root directory of the project (Inside cloned repository folder), run `pytest --cov=app`

### Style Guide.
PEP 8

## Deployment
[Heroku](https://questioner-backend.herokuapp.com/)

## Built With
* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/) - The web framework used

## Authors
* **Kelyn Paul Njeri.** 

## Acknowledgments
* Andela Kenya.
* Andela Developer Challenge.




### Author
Kelyn Paul Njeri.
