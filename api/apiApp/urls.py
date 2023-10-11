from django.contrib import admin
from django.db import router
from django.urls import path,include
from apiApp.views import CompanyViewSet, EmployeeeViewSet
from rest_framework import routers,serializers,viewsets


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees',EmployeeeViewSet)

urlpatterns = [
    path('',include(router.urls))
]
