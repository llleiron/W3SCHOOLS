from django.shortcuts import render
from rest_framework import generics
from db.serializers import CustomerDetailSerializer , CustomersListSerializer , ShippersDetailSerializer , ShippersListSerializer , EmployeeDetailSerializer , EmployeesListSerializer
from db.models import Customers , Shippers , Employees
# Create your views here.

class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerDetailSerializer

class CustomersListView(generics.ListAPIView):
    serializer_class = CustomersListSerializer
    queryset = Customers.objects.all()

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerDetailSerializer
    queryset = Customers.objects.all()


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeDetailSerializer

class EmployeesListView(generics.ListAPIView):
    serializer_class = EmployeesListSerializer
    queryset = Employees.objects.all()

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employees.objects.all()


class ShipperCreateView(generics.CreateAPIView):
    serializer_class = ShippersDetailSerializer

class ShippersListView(generics.ListAPIView):
    serializer_class = ShippersListSerializer
    queryset = Shippers.objects.all()

class ShipperDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShippersDetailSerializer
    queryset = Shippers.objects.all()