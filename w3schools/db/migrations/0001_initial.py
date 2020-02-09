# Generated by Django 3.0.2 on 2020-02-08 10:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=64, verbose_name='CustomerName')),
                ('ContactName', models.CharField(max_length=64, verbose_name='ContactName')),
                ('Address', models.CharField(max_length=64, verbose_name='Addres')),
                ('City', models.CharField(max_length=64, verbose_name='City')),
                ('PostalCode', models.CharField(max_length=64, verbose_name='PostalCode')),
                ('Country', models.CharField(max_length=64, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=64, verbose_name='LastName')),
                ('FirstName', models.CharField(max_length=64, verbose_name='FirstName')),
                ('BirthDate', models.DateField(verbose_name='BirthDate')),
                ('Photo', models.FileField(upload_to='', verbose_name='Photo')),
                ('Notes', models.CharField(max_length=500, verbose_name='Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShipperName', models.CharField(max_length=64, verbose_name='CustomerName')),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
    ]