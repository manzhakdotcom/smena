from django.contrib import admin

from station.models import Circle, SHCH, Station

# Register your models here.


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_dispalay = ['name']


@admin.register(SHCH)
class SHCHAdmin(admin.ModelAdmin):
    list_dispalay = ['name']


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_dispalay = ['name']
