from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customers(models.Model):
    CustomerName = models.CharField(verbose_name='CustomerName', max_length=64)
    ContactName = models.CharField(verbose_name='ContactName', max_length=64)
    Address = models.CharField(verbose_name='Addres', max_length=64)
    City = models.CharField(verbose_name='City', max_length=64)
    PostalCode = models.CharField(verbose_name='PostalCode', max_length=64)
    Country = models.CharField(verbose_name='Country', max_length=64)

class Employees(models.Model):
    LastName = models.CharField(verbose_name='LastName', max_length=64)
    FirstName = models.CharField(verbose_name='FirstName', max_length=64)
    BirthDate = models.DateField(verbose_name='BirthDate')
    Photo = models.FileField(verbose_name='Photo')
    Notes = models.CharField(verbose_name='Notes', max_length=500)
    

class Shippers(models.Model):
    ShipperName = models.CharField(verbose_name='CustomerName', max_length=64)
    Phone =  PhoneNumberField(blank=True)
