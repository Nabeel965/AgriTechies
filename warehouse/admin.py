from django.contrib import admin

# Register your models here.
from .models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_name', 'location', 'no_of_rooms', 'room_capacity', 'available_capacity', 'pub_date')


admin.site.register(Warehouse, WarehouseAdmin)
