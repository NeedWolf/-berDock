from home.models import *
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

class TestModels(TestCase):
    def failTest(self):
        assert 1 == 2

    def test_App(self):
        client = Client()


    def test_AppRequest(self):
        client = Client()
