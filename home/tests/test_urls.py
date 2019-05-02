from django.test import SimpleTestCase
from home.views import AppView, SearchView, AppDetailView, AppUpdateView, AppCreateView

class TestUrls(SimpleTestCase):
    def test_url(self):
        assert 1 == 2
        name = "AppName"
        self.assertEquals(resolve(name).func, AppView)

        name = "AppSearch"
        self.assertEquals(resolve(name).func, SearchView)

        name = "AppDetails"
        self.assertEquals(resolve(name).func, AppDetailView)

        name = "AppUpdateString"
        self.assertEquals(resolve(name).func, AppUpdateView)

        name = "App Create View"
        self.assertEquals(resolve(name).func, AppCreateView)
