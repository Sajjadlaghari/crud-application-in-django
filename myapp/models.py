from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=130)
    class Meta:
        db_table = 'employees'


# Create your models here.
