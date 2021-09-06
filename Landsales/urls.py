from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='landsales'),
    path('<int:landsale_id>', views.landsale, name='landsale'),
]