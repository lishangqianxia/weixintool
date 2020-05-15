from django.contrib import admin
from django.urls import path, include
from .views import weather, menu, simpleweather, image, service


urlpatterns = [
    # path('', weather.helloworld),
    # path('', weather.weather),
    path('s', simpleweather.SimpleWeather.as_view()),
    path('weather', weather.WeatherView.as_view()),
    path('menu', menu.get_menu),
    path('image', image.ImageView.as_view()),
    path('image/list', image.ImageListView.as_view()),
    path('stock', service.stock),
    path('constellation', service.constellation),
    path('joke', service.joke)
]
