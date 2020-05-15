# -*-encoding=utf8 -*-

from django.contrib import admin
from django.urls import path, include
from authorization import views


urlpatterns = [
    path('service/', include('apis.urls')),
    path('authorize', views.authorize, name='authorize'),
    path('auth/', include('authorization.urls'))
]
