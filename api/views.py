from rest_framework.response import Response
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework import viewsets
from django.db.models import Count
from rest_framework.decorators import action


# Company Views 
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.annotate(total_employees = Count('employees')).all()
    serializer_class = CompanySerializer

   
        

# Employee Views

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('company').all()
    serializer_class = EmployeeSerializer