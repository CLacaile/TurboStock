from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from app.models import *
from app.views import *

EMAIL = "Test"
PASSWORD = "Test"
WRONG_PASSWORD = "wrongTest"
WRONG_EMAIL = "wrongTest"


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(first_name="test", last_name="test", email=EMAIL, password=PASSWORD)


    def test_authentication_ok(self):
        response = self.client.post('/authenticate/', {"email": EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"], self.user)

    def test_authentication_wrong_email(self):
        response = self.client.post('/authenticate/', {"email": WRONG_EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())


    def test_authentication_wrong_password(self):
        response = self.client.post('/authenticate/', {"email": EMAIL, "password": WRONG_PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())

    def test_authenticated_view_authenticated(self):
        request = self.factory.get('/home/')
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_view_not_authenticated(self):
        request = self.factory.get('/home/')
        request.user = AnonymousUser()
        response = home(request)
        self.assertEqual(response.status_code, 401)

