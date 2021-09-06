from django.contrib import admin
from .models import Automobile
# Register your models here.

class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('id','carName','modelyear')
    list_display_links = ('id','carName')
admin.site.register(Automobile, AutomobileAdmin)