from django.db import models
from django.urls import reverse
from django.conf import settings
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


class Comment(models.Model):
    app = models.ForeignKey(
       App,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('com_new')

class AddComment(models.Model):
    app = models.CharField(max_length=255)
    comment = models.CharField(max_length=140)
    author = models.CharField(max_length=255)


