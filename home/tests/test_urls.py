from django.test import SimpleTestCase
from home.views import AppView, SearchView, AppDetailView, AppUpdateView, AppCreateView

class TestUrls(SimpleTestCase):
    def test_AppView(self):
        assert 1 == 2
        name = "AppName"
        self.assertEquals(resolve(name).func, AppView)

    def test_AppSearch(self):
        name = "AppSearch"
        self.assertEquals(resolve(name).func, SearchView)

    def test_AppDetailView(self):
        name = "AppDetails"
        self.assertEquals(resolve(name).func, AppDetailView)

    def test_AppUpdate(self):
        name = "AppUpdateString"
        self.assertEquals(resolve(name).func, AppUpdateView)

    def test_AppCreate(self):
        name = "App Create View"
        self.assertEquals(resolve(name).func, AppCreateView)
