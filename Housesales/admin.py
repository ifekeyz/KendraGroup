from django.contrib import admin

from .models import Housesale

class HousesaleAdmin(admin.ModelAdmin):
    list_display = ('id','location','team')
    list_display_links = ('id','location')
admin.site.register(Housesale, HousesaleAdmin)

