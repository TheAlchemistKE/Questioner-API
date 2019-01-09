"""Module for Testing the Question Endpoints."""
import json

# Local Import
from .basecase import TestBaseCase as base

class TestQuestion(base):
    """Testing the Question Endpoints with valid input."""
    def setUp(self):
        base.setUp(self)

    def test_create_question(self):
        """Testing Creation of a Question."""
            
        response = self.client.post('/api/v1/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "Question was created successfully.")

    def test_fetch_all_questions(self):
        """Test fetching all questions."""
        post_response = self.client.post('/api/v1/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_data["message"], "Question was created successfully.")
        # Fetching all questions.
        response = self.client.get('/api/v1/questions', content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_question(self):
        """Test fetching a single question"""
