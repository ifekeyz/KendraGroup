from django.contrib import admin

# Register your models here.
from .models import Consulting

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location','phone')
    list_display_links = ('name','location')
admin.site.register(Consulting, ConsultingAdmin)
