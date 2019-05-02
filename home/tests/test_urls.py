from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *

class TestUrls(SimpleTestCase):
    def test_failure(self):
        # This one SHOULD FAIL PLEASE DO NOT TAKE OUT
        # This tells us if the test is running
        assert 1 == 2

    def test_AppView(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func.view_class, AppView)

    def test_AppSearch(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_AppDetailView(self):
        url = reverse("post_detail", args = [5])
        self.assertEquals(resolve(url).func.view_class, AppDetailView)

    def test_AppUpdate(self):
        # bug found
        # Getting AppDetail instead of AppUpdate
        url = reverse("apost_new")
        self.assertEquals(resolve(url).func.view_class, AllappCreateView)

    def test_AppCreate(self):
        url = reverse("apost_detail", args = [1])
        self.assertEquals(resolve(url).func.view_class, AllappDetailView)