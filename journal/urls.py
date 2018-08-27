from django.urls import path

from journal.views import detail, write_down, write_out, extra_write_out

app_name = 'journal'
urlpatterns = [
    path('detail/<int:write_down_id>', detail, name='detail'),
    path('add/write-down', write_down, name='add/write-down'),
    path('add/write-out/<int:write_down_id>', write_out, name='add/write-out'),
    path('add/extra-write-out/<int:write_down_id>', extra_write_out, name='add/extra-write-out'),
]
