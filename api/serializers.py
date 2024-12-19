from rest_framework import serializers
from .models import Company,Employee

# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    total_employees = serializers.IntegerField()
    
    class Meta:
        model = Company
        fields = ['company_id','name','location','about','type','added_date','active','total_employees']
        
        
        
# Employee Serializer

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name',read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id','name','email','address','phone_Number','about','position','company']
        
        