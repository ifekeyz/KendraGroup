from django.contrib import admin

# Register your models here.
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','email','timestamp')
    list_display_links = ('email',)
admin.site.register(Signup,SignupAdmin)
