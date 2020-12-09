from django.db import models
import datetime
import time
from django.utils import timezone


# Create your models here.
class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    no_of_rooms = models.CharField(max_length=200)
    room_no = models.CharField(max_length=200)
    room_length = models.CharField(max_length=200)
    room_width = models.CharField(max_length=200)
    room_height = models.CharField(max_length=200)
    room_capacity = models.CharField(max_length=200)
    available_capacity = models.CharField(max_length=200)
    product_already_stored = models.CharField(max_length=200)
    refrigerant = models.CharField(max_length=200)
    room_temperature = models.CharField(max_length=200)
    relative_humidity = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.warehouse_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
