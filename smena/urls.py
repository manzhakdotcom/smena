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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from journal.views import index
from journal import urls as journal_urls
from station import urls as station_urls
from duty import urls as duty_urls
from archive import urls as archive_urls
from staff import urls as staff_urls
from stats import urls as stats_urls

urlpatterns = [
    #
    path('admin/', admin.site.urls),
    # Main pages
    path('', index, name='index'),
    # Add pages
    path('journal/', include(journal_urls, namespace='journal')),
    path('station/', include(station_urls, namespace='station')),
    path('duty/', include(duty_urls, namespace='duty')),
    path('archive/', include(archive_urls, namespace='archive')),
    path('staff/', include(staff_urls, namespace='staff')),
    path('stats/', include(stats_urls, namespace='stats')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
