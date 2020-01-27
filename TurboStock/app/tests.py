from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from app.models import *
from app.views import *

CEO_EMAIL = "ceoEmail"
AISLE_MANAGER_EMAIL = "aisleManagerEmail"
STORE_MANAGER_EMAIL = "storeManagerEmail"
PASSWORD = "Password$$$"
WRONG_PASSWORD = "wrongTest"
WRONG_EMAIL = "wrongTest"


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.storeManager = StoreManager.objects.create(first_name="test", last_name="test", email=STORE_MANAGER_EMAIL,
                                                        password=PASSWORD)
        self.aisleManager = AisleManager.objects.create(first_name="test", last_name="test", email=AISLE_MANAGER_EMAIL,
                                                        password=PASSWORD)
        self.ceo = CEO.objects.create(first_name="test", last_name="test", email=CEO_EMAIL, password=PASSWORD)

    def test_authentication_ok(self):
        response = self.client.post('/authenticate/', {"email": STORE_MANAGER_EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].id, self.storeManager.id)

        response = self.client.post('/authenticate/', {"email": AISLE_MANAGER_EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].id, self.aisleManager.id)

        response = self.client.post('/authenticate/', {"email": CEO_EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].id, self.ceo.id)

    def test_authentication_empty_form(self):
        response = self.client.post('/authenticate/', {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.context["user"].id, self.storeManager.id)

        response = self.client.post('/authenticate/', {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.context["user"].id, self.aisleManager.id)

        response = self.client.post('/authenticate/', {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.context["user"], self.ceo)

    def test_authentication_wrong_email(self):
        response = self.client.post('/authenticate/', {"email": WRONG_EMAIL, "password": PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())

    def test_authentication_wrong_password(self):
        response = self.client.post('/authenticate/', {"email": STORE_MANAGER_EMAIL, "password": WRONG_PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())

        response = self.client.post('/authenticate/', {"email": AISLE_MANAGER_EMAIL, "password": WRONG_PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())

        response = self.client.post('/authenticate/', {"email": CEO_EMAIL, "password": WRONG_PASSWORD})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.context["user"], AnonymousUser())

    def test_authenticated_view_authenticated(self):
        request = self.factory.get('/home/')
        request.user = self.ceo
        response = home(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/home/')
        request.user = self.aisleManager
        response = home(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/home/')
        request.user = self.storeManager
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_view_not_authenticated(self):
        request = self.factory.get('/home/')
        request.user = AnonymousUser()
        response = home(request)
        self.assertEqual(response.status_code, 401)


class StoreTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.storeManager = StoreManager.objects.create(first_name="test", last_name="test", email=STORE_MANAGER_EMAIL,
                                                        password=PASSWORD)
        self.aisleManager = AisleManager.objects.create(first_name="test", last_name="test", email=AISLE_MANAGER_EMAIL,
                                                        password=PASSWORD)
        self.ceo = CEO.objects.create(first_name="test", last_name="test", email=CEO_EMAIL, password=PASSWORD)

    def test_access_create_store_page_ok(self):
        request = self.factory.get('/store/new')
        request.user = self.ceo
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_access_create_store_page_not_authenticated(self):
        request = self.factory.get('/store/new')
        request.user = AnonymousUser()
        response = home(request)
        self.assertEqual(response.status_code, 401)

    def test_access_create_store_page_not_allowed(self):
        request = self.factory.get('/store/new')
        request.user = self.aisleManager
        response = home(request)
        self.assertEqual(response.status_code, 401)

        request = self.factory.get('/store/new')
        request.user = self.storeManager
        response = home(request)
        self.assertEqual(response.status_code, 401)

    def test_create_store_ok(self):
        request = self.factory.post('/store/create', {"address": "3 rue de Brest", "city": "Rennes"})
        request.user = self.ceo
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_create_store_empty_fields(self):
        request = self.factory.post('/store/create', {})
        request.user = self.ceo
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_create_store_not_authenticated(self):
        request = self.factory.get('/store/create', {})
        request.user = AnonymousUser()
        response = home(request)
        self.assertEqual(response.status_code, 401)

    def test_create_store_not_allowed(self):
        request = self.factory.get('/store/create', {})
        request.user = self.storeManager
        response = home(request)
        self.assertEqual(response.status_code, 401)

        request = self.factory.get('/store/create', {})
        request.user = self.aisleManager
        response = home(request)
        self.assertEqual(response.status_code, 401)
