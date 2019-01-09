"""
    Question Models
    Author: Kelyn Paul Njeri.
"""
import json
from datetime import datetime

class QuestionModel():
    """Question Model."""
    questions = []
    def __init__(self, user, meetup, title, body):
        """Question Model class constructor."""
        # TODO: Link Questions to users to get the user who posted the question
        self.question_id = len(QuestionModel.questions) + 1
        self.created_on = json.dumps(datetime.now(), default=str)
        self.user = user
        self.meetup = meetup
        self.title = title
        self.body = body

    def create_question_record(self):
        """Creating Question Record."""
        new_question = dict(
            id=self.question_id,
            createdOn=self.created_on,
            user=self.user,
            meetup=self.meetup,
            title=self.title,
            body=self.body
        )
        self.questions.append(new_question)
        return new_question
