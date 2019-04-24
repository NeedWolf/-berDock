from django.contrib import admin
from home.models import App, AppRequest


class HomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(App, HomeAdmin)
admin.site.register(AppRequest, HomeAdmin)