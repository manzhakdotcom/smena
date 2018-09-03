from django.contrib import admin
from staff.models import Organization, Position, Employee

# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_dispalay = ['abbr', 'name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_dispalay = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_dispalay = ['surname', 'organization']