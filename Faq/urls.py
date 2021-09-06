from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='faq'),
    path('message',views.message, name='message')
]