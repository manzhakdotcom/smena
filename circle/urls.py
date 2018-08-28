from django.urls import path

from circle.views import index

app_name = 'circle'
urlpatterns = [
    path('', index, name='index'),
]
