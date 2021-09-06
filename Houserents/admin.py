from django.contrib import admin

# Register your models here.
from .models import Houserent

class HouserentAdmin(admin.ModelAdmin):
    list_display = ('id','location','team')
    list_display_links = ('id','location')
admin.site.register(Houserent, HouserentAdmin)
