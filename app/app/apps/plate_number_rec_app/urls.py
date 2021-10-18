from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

app_name = 'plate_number_rec_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('success', views.success, name='success'),
    path('clear', views.clear, name='clear'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
