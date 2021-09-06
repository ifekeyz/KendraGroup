from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='houserents'),
    path('<int:houserent_id>', views.houserent, name='houserent'),
]