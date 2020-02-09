from django.contrib import admin
from django.urls import path, include
from db.views import *

urlpatterns = [
path('Customer/create', CustomerCreateView.as_view()),
path('Customer/all', CustomersListView.as_view()),
path('Customer/detail/<int:pk>', CustomerDetailView.as_view()),

path('Shipper/create', ShipperCreateView.as_view()),
path('Shipper/all', ShippersListView.as_view()),
path('Shipper/detail/<int:pk>', ShipperDetailView.as_view()),

path('Employee/create', EmployeeCreateView.as_view()),
path('Employee/all', EmployeesListView.as_view()),
path('Employee/detail/<int:pk>', EmployeeDetailView.as_view()),
]
