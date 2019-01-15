import json
from ddt import ddt, data

from .basecase import TestBaseCase as base

@ddt
class TestAuthentication(base):
    """Testing Authentication endpoint"""
    def setUp(self):
        base.setUp(self)

    def test_user_registration(self):
        """Testing User Registration."""
        response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload1), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "User registered successfully. Please Log in.")
    
    def test_user_login(self):
        """Testing Logging In."""
        post_response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload2), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_data["message"], "User registered successfully. Please Log in.")
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.login_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["message"], "User login successful.")      

    def test_logging_in_non_existent_user(self):
        """Testing Logging in a non-existent user."""
        post_response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_data["message"], "User registered successfully. Please Log in.")
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.bad_login_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["error"], "User does not exist.")

    def testing_register_existing_user(self):
        response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response_data["message"], "Use another email or login.")
    @data({
            "firstname": "Kelyn",
            "lastname": "",
            "othername": "Paul",
            "email": "example123@gmail.com",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test@12345",
            "password2": "Test@12345"
        },
        {
            "firstname": " ",
            "lastname": "Njeri",
            "othername": "Paul",
            "email": "example12378@gmail.com",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test@12345",
            "password2": "Test@12345"
        })
    def testing_entering_wrong_inputs(self, value):
        response = self.client.post('/api/v1/auth/register', data=json.dumps(value), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Fields cannot be empty or spaces.")
    @data(
        {
            "firstname": "Kelyn",
            "lastname": "Njeri",
            "othername": "Paul",
            "email": "example12378@gmail.com",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test2345",
            "password2": "Test@12345"
        }
    )
    def testing_wrong_password(self, value):
        response = self.client.post('/api/v1/auth/register', data=json.dumps(value), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Enter correct email. Passwords must match.")

    @data({
            "firstname": "Kelyn",
            "lastname": "Njeri",
            "othername": "Paul",
            "email": "example123@gmailcom",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test@12345",
            "password2": "Test@12345"
        },
        {
            "firstname": "Kelyn",
            "lastname": "Njeri",
            "othername": "Paul",
            "email": "example12gmail.com",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test@12345",
            "password2": "Test@12345"
        })
    def testing_wrong_email(self, value):
        response = self.client.post('/api/v1/auth/register', data=json.dumps(value), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Enter correct email. Passwords must match.")
    