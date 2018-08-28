from django.urls import path

from archive.views import index

app_name = 'archive'
urlpatterns = [
    path('', index, name='index'),
]
