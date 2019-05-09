from django.test import TestCase
from home.models import *


class TestModels(TestCase):

    def test_failure(self):
        assert 1 == 2

    def setUp(self):
        App.objects.create(title = "UberDock", blurb = "Scott was here", link = "www.google.com")
        AppRequest.objects.create(title= "UberDock2", blurb = "Alex was here", link = "www.bing.com")

    def test_app_title(self):
        app = App.objects.get(id=1)
        expected_object_title = f'{app.title}'
        self.assertEquals(expected_object_title, 'UberDock')

    def test_app_blurb(self):
        app = App.objects.get(id=1)
        expected_object_blurb = f'{app.blurb}'
        self.assertEquals(expected_object_blurb, 'Scott was here')

    def test_app_link(self):
        app = App.objects.get(id=1)
        expected_object_link = f'{app.link}'
        self.assertEquals(expected_object_link, 'www.google.com')

    def test_appRequest_title(self):
        appRequest = AppRequest.objects.get(id = 1)
        expected_object_title = f'{appRequest.title}'
        self.assertEquals(expected_object_title, "UberDock2")

    def test_appRequest_blurb(self):
        appRequest = AppRequest.objects.get(id = 1)
        expected_object_blurb = f'{appRequest.blurb}'
        self.assertEquals(expected_object_blurb, "Alex was here")

    def test_appRequest_link(self):
        appRequest = AppRequest.objects.get(id = 1)
        expected_object_link = f'{appRequest.link}'
        self.assertEquals(expected_object_link, "www.bing.com")