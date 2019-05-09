from django.test import TestCase, Client
from django.urls import reverse
from home.models import App, AppRequest
from home.views import AppView, AppCreateView, AppDetailView, AppUpdateView, SearchView, AllappCreateView, AllappDetailView, AllappView
import json
class TestViews(TestCase):
    # test designed to fail, first off.
    def setUp(appName, appBlurb, appLink, appCategory):
        App.objects.create(title=appName, blurb=appBlurb, link=appLink, appCategory=appCategory)

    def test_project_get_SELF(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_AppViews(self):
        client = Client()

        response = client.get(reverse(AppView.template_name))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    def test_AppCreateView(self):
        client = Client()

        response = client.get(reverse(AppCreateView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_new.html')

    def test_AppDetailView(self):
        client = Client()

        response = client.get(reverse(AppDetailView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_AppUpdateView(self):
        client = Client()

        response = client.get(reverse(AppUpdateView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_search.html')

    def test_SearchView(self):
        client = Client()

        response = client.get(reverse(SearchView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_AllappCreateView(self):
        client = Client()

        response = client.get(reverse(AllappCreateView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'apost_new.html')

    def test_AllappDetailView(self):
        client = Client()

        response = client.get(reverse(AllappDetailView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'apost_detail.html')

    def test_AllappView(self):
        client = Client()

        response = client.get(reverse(AllappView.template_name))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_app.html')