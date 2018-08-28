from django.urls import path

from duty.views import index

app_name = 'duty'
urlpatterns = [
    path('', index, name='index'),
]
