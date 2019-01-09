"""Question Views Module."""
# Third Party Imports.
import json
from flask_restplus import reqparse, Resource
from flask import Response
import json

# Local Imports.
from ..models.question_model import QuestionModel
from ..utils.validator import QuestionDataTransferObject

question_api = QuestionDataTransferObject.question_namespace

parser = reqparse.RequestParser()
parser.add_argument("user", required=True, help="Enter the user id.")
parser.add_argument("meetup", required=True, help="Enter the meetup id.")
parser.add_argument("title", required=True, help="Add Question Title.")
parser.add_argument("body", required=True, help="Add Question Body.")

question_request_model = QuestionDataTransferObject.question_request_model

@question_api.route('')
class QuestionList(Resource):
    """Question Endpoint."""
    @question_api.expect(question_request_model, validate=True)
    def post(self):
        """POST request."""
        request_data = parser.parse_args()
        user = request_data["user"]
        meetup = request_data["meetup"]
        title = request_data["title"]
        body = request_data["body"]

        new_question = QuestionModel(user, meetup, title, body)
        save_question = new_question.create_question_record()
        response_payload = dict(
            status=201,
            message="Question was created successfully.",
            data=save_question
        )
        response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
        return response

    def get(self):
        """Fetch All Questions.""" 
        questions = QuestionModel.fetch_all_questions(self)
        response_payload = {
            "status": 200,
            "data": questions
        }
        response = Response(json.dumps(response_payload), status=200, mimetype="application/json")
        return response


