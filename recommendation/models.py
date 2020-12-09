from django.db import models
import datetime
import time
from django.utils import timezone


# Create your models here.

class crop_data(models.Model):
    crop_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.crop_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
