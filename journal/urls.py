from django.urls import path

from journal.views import add, write_down, write_out, extra_write_out

app_name = 'journal'
urlpatterns = [
    path('add/', add, name='add/index'),
    path('add/write-down', write_down, name='add/write-down'),
    path('add/write-out', write_out, name='add/write-out'),
    path('add/extra-write-out', extra_write_out, name='add/extra-write-out'),
]
