from django.test import TestCase
from django.urls import reverse
from .models import App


def create_app(app_title, app_blurb, app_url):
    return App.objects.create(title=app_title, blurb=app_blurb)
def requestApp(app_title, app_blurb, app_url):
    return AppRequest(name = app_title, fields = app_blurb)

class AppTestCase(TestCase):
    # Creating an app
    def testing_app_created(self):
        future_app = create_app("Test", "Blurb1", "google.com")


class AppRequestTestCase(TestCase):
     # Sending an app request
    def testing_app_requested(self):
        requestedApp1 = requestApp("","","") # fail case (attempt) located here
        requested_app = requestApp("Test: App Request","Blurbity Blurb Blurb 42","google.com") #what Should succeed is here




