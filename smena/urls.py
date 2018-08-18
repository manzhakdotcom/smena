"""smena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from journal.views import (index, content)
from journal.views import (add, write_down, WriteOut, extra_write_out)

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add/index'),
    path('add/write-down', write_down, name='add/write-down'),
    path('add/write-out', WriteOut.as_view(), name='add/write-out'),
    path('add/extra-write-out', extra_write_out, name='add/extra-write-out'),
    path('<int:val>', content, name='content'),
    path('admin/', admin.site.urls),
]
