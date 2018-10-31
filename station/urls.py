from django.urls import path

from station.views import index

app_name = 'station'
urlpatterns = [
    path('', index, name='index'),
]
