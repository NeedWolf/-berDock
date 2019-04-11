from django.db import models

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title