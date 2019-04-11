from django.contrib import admin
from home.models import App

class HomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(App, HomeAdmin)