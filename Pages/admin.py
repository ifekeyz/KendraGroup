from django.contrib import admin
from .models import Team, Slider

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_mvp')
    list_display_links = ('id','name')
    list_editable = ('is_mvp',)

admin.site.register(Team, TeamAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','SliderName','is_published')
    list_display_links = ('id','SliderName')
    list_editable = ('is_published',)

admin.site.register(Slider, SliderAdmin)
