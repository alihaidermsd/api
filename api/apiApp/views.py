from django.shortcuts import render,redirect,HttpResponse
from rest_framework import viewsets
from apiApp.models import Company,Employee
from apiApp.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class= CompanySerializer

    @action (detail=True, methods=['get'])
    def employees(self, request , pk=None):
        
        try:
            company = Company.objects.get(pk=pk)
            emps= Employee.objects.filter(company=company)
            emps_serializer= EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except:
            return Response({'Company Does not Exist'})

    
        pass

class EmployeeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer