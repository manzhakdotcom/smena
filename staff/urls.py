from django.urls import path

from staff.views import index

app_name = 'staff'
urlpatterns = [
    path('', index, name='index'),
]
