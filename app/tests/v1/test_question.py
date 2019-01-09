"""Module for Testing the Question Endpoints."""
import json

# Local Import
from .basecase import TestBaseCase as base

class TestQuestion(base):
    """Testing the Meetup Endpoints with valid input."""
    def setUp(self):
        base.setUp(self)

    def test_create_question(self):
        """Testing Creation of a Meetup."""
            
        response = self.client.post('/api/v1/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "Question was created successfully.")
