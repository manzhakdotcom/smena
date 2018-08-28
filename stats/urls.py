from django.urls import path

from stats.views import index

app_name = 'stats'
urlpatterns = [
    path('', index, name='index'),
]
