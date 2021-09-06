from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='automobiles'),
    path('<int:automobile_id>', views.automobile, name='automobile'),
]