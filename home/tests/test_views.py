from django.test import TestCase, Client
from django.urls import reverse
from home.models import App, AppRequest
import json
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.list_url = reverse('list')
        self.detail_url = reverse('detail')

    def test_project_get_SELF(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')