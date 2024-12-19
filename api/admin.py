from django.contrib import admin
from .models import Company,Employee



class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','type','added_date','active']
    ordering = ['-added_date','-active']
    
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_Number','position','company']


    
    
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)