from django.urls import path

from duty.views import index, detail

app_name = 'duty'
urlpatterns = [
    path('', index, name='index'),
    path('detail/', detail, name='detail'),
]
