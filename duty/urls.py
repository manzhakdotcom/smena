from django.urls import path

from duty.views import form
app_name = 'duty'
urlpatterns = [
    path('', form, name='form'),
]
