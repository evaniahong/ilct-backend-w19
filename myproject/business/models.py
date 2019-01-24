# Create your models here.
from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length = 200)
    gps_x = models.DecimalField(max_digits=15, decimal_places=7)
    gps_y = models.DecimalField(max_digits=15, decimal_places=7)
    address = models.CharField(max_length = 200)
    student_discount = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 200)

    def __str__(self):
        return self.business_name

