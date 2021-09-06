from django.contrib import admin

# Register your models here.
from .models import FAQs, Message

class FAQsAdmin(admin.ModelAdmin):
    list_display = ('id','question')
    list_display_links = ('id','question')
    list_per_page = 15
admin.site.register(FAQs, FAQsAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_links = ('name','email')
    list_per_page = 10
admin.site.register(Message, MessageAdmin)