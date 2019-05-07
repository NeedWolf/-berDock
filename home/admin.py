from django.contrib import admin
from home.models import App, AppRequest
from . import models

class HomeAdmin(admin.ModelAdmin):
    pass

class CommentInline(admin.TabularInline):
    model = models.Comment
class HomeAdmin(admin.ModelAdmin):
    inlines = [ CommentInline, ]




admin.site.register(models.App, HomeAdmin)
admin.site.register(AppRequest)
admin.site.register(models.Comment)