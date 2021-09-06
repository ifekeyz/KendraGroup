from django.contrib import admin
from .models import Landsale
# Register your models here.
class LandsaleAdmin(admin.ModelAdmin):
    list_display = ('id','location','landsize')
    list_display_links = ('id','location')
admin.site.register(Landsale, LandsaleAdmin)
