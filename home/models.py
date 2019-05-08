from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]

        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class App(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField(max_length=255)
    link = models.URLField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

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


