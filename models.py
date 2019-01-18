from django.conf import settings
from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
	business_name = models.CharField(max_length=128)
	gps_x = models.FloatField()
	gps_y = models.FloatField()
	address = models.TextField()
	discount = models.TextField()
	phone_num = models.CharField(max_length=15)
	created_date = models.DateTimeField(default=timezone.now)
	website = models.URLField()

