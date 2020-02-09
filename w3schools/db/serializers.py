from rest_framework import serializers
from db.models import Customers , Shippers , Employees

class CustomersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('__all__')

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('__all__')

class ShippersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = ('__all__')

class ShippersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = ('__all__')

class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('__all__')

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('__all__')