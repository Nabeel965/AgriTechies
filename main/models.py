from django.db import models
import datetime
import time
from django.utils import timezone


# Create your models here.

class Crop(models.Model):
    product_type = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    crop_stage = models.CharField(max_length=200)
    total_crop_quantity = models.CharField(max_length=200)
    daily_loading = models.CharField(max_length=200)
    required_temperature = models.CharField(max_length=200)
    required_relative_humidity = models.CharField(max_length=200)
    duration_of_storage = models.CharField(max_length=200)
    pick_up_location = models.CharField(max_length=200)
    drop_off_location = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Crop, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
