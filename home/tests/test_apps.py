from django.test import TestCase, Client
from django.urls import reverse, resolve
from home.models import App, AppRequest
from home.apps import HomeConfig

# not sure how this one would work, but based on the fact there's only one class, well😅
class TestApps(TestCase):
    def setUp(self):
        client = Client()
        assert 1 == 2

    def test_HomeConfig(self):
        client = Client()

        Home = reversed(HomeConfig.home)
        self.assertEquals(resolve(Home).func.view_class, HomeConfig)