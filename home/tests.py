from django.test import TestCase
from django.urls import reverse
from .models import App


def create_app(app_title, app_blurb, app_url):
    return App.objects.create(title=app_title, blurb=app_blurb)

class AppTestCase(TestCase):
    # Creating an app
    # Test 1: Viewing the app
    def testing_app_created(self):
        future_app = create_app("Test", "Blurb1", "google.com")





