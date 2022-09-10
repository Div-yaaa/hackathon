from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ("full_name", "last_login")
    list_filter = ("full_name", "last_login")


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("developer_name", "role", "year_of_experience")
    search_fields = ['company_id', 'role', 'tech_stack']
    list_filter = ("developer_name", "role")


@admin.register(Cilent)
class CilentAdmin(admin.ModelAdmin):
    list_display = ("cilent_name", )


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ("project_name", "project_role")

class Runtime(admin.AdminSite):
    site_header = 'RUNTIME_BUSINESS'
