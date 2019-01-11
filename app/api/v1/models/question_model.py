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
        self.votes = 0

    def create_question_record(self):
        """Creating Question Record."""
        new_question = dict(
            id=self.question_id,
            createdOn=self.created_on,
            user=self.user,
            meetup=self.meetup,
            title=self.title,
            body=self.body,
            votes=self.votes
        )
        self.questions.append(new_question)
        return new_question

    def fetch_all_questions(self):
        """Fetching all questions."""
        return QuestionModel.questions

    @staticmethod
    def fetch_specific_question(question_id):
        """Fetching Specific Questions"""
        all_questions = QuestionModel.questions
        single_question = [question for question in all_questions if question["id"] == question_id]
        if single_question:
            return single_question
        else:
            return "Question does not exit. Please add it."

    def upvote_question(self, question_id):
        """Upvote question"""
        questions = QuestionModel.questions
        upvote_question = [question for question in questions if question["id"] == question_id]
        if upvote_question:
            upvote_question[0]["votes"] = upvote_question[0]["votes"] + 1
            return upvote_question
        else:
            return "Question does not exist."

    def downvote_question(self, question_id):
        """Upvote question"""
        questions = QuestionModel.questions
        downvote_question = [question for question in questions if question["id"] == question_id]
        if downvote_question:
            downvote_question[0]["votes"] = downvote_question[0]["votes"] - 1
            return downvote_question
        else:
            return "Question does not exist."
