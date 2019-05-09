from django.test import TestCase, Client
from home.models import App, AppRequest
from home.apps import HomeConfig

# not sure how this one would work, but based on the fact there's only one class, well😅
class TestApps(TestCase):
    def setUp(self):
        client = Client()

    def test_failure(self):
        assert 1 == 2

    def test_HomeConfig(self):
        client = Client()
        home = HomeConfig.name
        self.assertEquals(home, "home")