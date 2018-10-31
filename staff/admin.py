from django.contrib import admin
from staff.models import Organization, Position, Employee, Workplace

# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['abbr', 'name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['surname', 'organization']


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ['name']
