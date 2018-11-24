from django.urls import path

from journal.views import detail, delete, write_down, write_out, extra_write_out, edit_write_down, edit_write_out, edit_extra_write_out

app_name = 'journal'
urlpatterns = [
    path('detail/<int:write_down_id>/', detail, name='detail'),
    path('add/write-down/', write_down, name='add/write-down'),
    path('add/write-out/<int:write_down_id>/', write_out, name='add/write-out'),
    path('add/extra-write-out/<int:write_down_id>/', extra_write_out, name='add/extra-write-out'),
    path('edit/write-down/<int:write_down_id>/', edit_write_down, name='edit/write-down'),
    path('edit/write-out/<int:write_out_id>/', edit_write_out, name='edit/write-out'),
    path('edit/extra-write-out/<int:extra_write_out_id>/', edit_extra_write_out, name='edit/extra-write-out'),
    path('delete/', delete, name='delete'),
]
