from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Subscrib.views import email_list_signup

urlpatterns = [
    path('',include('Pages.urls')),
    path('automobiles/',include('Automobiles.urls')),
    path('forms/',include('Form.urls')),
    path('houserents/',include('Houserents.urls')),
    path('housesales/',include('Housesales.urls')),
    path('landsales/',include('Landsales.urls')),
    path('faq/',include('Faq.urls')),
    path('subcribe/', email_list_signup, name='subscribe'),
    # path('subscribe/',include('Subscrib.urls')),
    path('consult/',include('Consult.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
