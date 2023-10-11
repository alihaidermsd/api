from django.contrib import admin

from apiApp.models import *

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)
admin.site.register (Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','position','company')
    list_filter=('company',)
admin.site.register(Employee, EmployeeAdmin)