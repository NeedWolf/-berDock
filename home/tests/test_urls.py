from django.test import SimpleTestCase
from home.views import AppView, SearchView, AppDetailView, AppUpdateView, AppCreateView

class TestUrls(SimpleTestCase):
    def test_url(self):
        assert 1 == 2
        name = "AppName"
        self.assertEquals(resolve(name).func, AppView)
