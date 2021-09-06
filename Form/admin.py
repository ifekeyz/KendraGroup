from django.contrib import admin
from .models import Forms
# Register your models here.

class FormsAdmin(admin.ModelAdmin):
    list_display = ('id','name','location','phone','sex')
    list_display_links = ('id','name','location')
admin.site.register(Forms,FormsAdmin )
