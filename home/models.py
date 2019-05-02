from django.db import models
from django.urls import reverse

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class AppRequest(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apost_detail', args=[str(self.id)])


