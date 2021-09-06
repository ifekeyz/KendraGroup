from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='housesales'),
    path('<int:housesale_id>', views.housesale, name='housesale'),
]