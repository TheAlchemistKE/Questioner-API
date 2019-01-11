[![Build Status](https://travis-ci.com/KelynPNjeri/Questioner-API.svg?branch=develop)](https://travis-ci.com/KelynPNjeri/Questioner-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/ff91486e5e85335922eb/maintainability)](https://codeclimate.com/github/KelynPNjeri/Questioner-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/KelynPNjeri/Questioner-API/badge.svg?branch=develop)](https://coveralls.io/github/KelynPNjeri/Questioner-API?branch=develop)
# Questioner API(Version 1)
Questioner web app, is an online platform that crowd-sources questions from users about meetups.

## API ENDPOINTS
#### Question Endpoints.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/questions  | Create a question for a specific meetup  | POST  |
| /api/v1/questions  | Get all questions for a specific meetup  | GET  |
| /api/v1/questions/<question-id> | Get a specific question  | GET  |
| /api/v1//questions/<question-id>/upvote  | Upvote a specific question.  | PATCH  |
|/api/v1/questions/<question-id>/downvote  | Downvote a specific question. | PATCH |

#### Meetup Endpoints
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v1/meetups  | Get all meetups  | GET  |
| /api/v1/meetups  | Create a meetup  | POST  |
|/api/v1/meetups/<meetup-id> | Get a specific meetup record  | GET  |
|/api/v1/meetups/<meetup-id>/rsvps  | Respond to meetup RSVP  | POST  |

## Getting Started
To get started:
1. Git clone the repository using `git clone https://github.com/KelynPNjeri/Questioner-API.git`

### Prerequisites
For the API to run smoothly tou will need the following:




### Author
Kelyn Paul Njeri.
