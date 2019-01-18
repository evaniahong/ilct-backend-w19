from django.db import models
from django.utils import timezone

class Buisness(models.Model):
    buisness_name = models.CharField(max_length=200)
    GPS_X = models.FloatField(default=0)
    GPS_Y = models.FloatField(default=0)
    address = models.CharField(max_length=200)
    student_discount = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())
    website = models.URLField(default="")

    def __str__(self):
        return self.buisness_name
