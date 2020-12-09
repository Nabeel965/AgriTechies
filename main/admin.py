from django.contrib import admin

# Register your models here.
from .models import Crop


class CropAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_type', 'crop_stage', 'total_crop_quantity', 'pub_date')


admin.site.register(Crop, CropAdmin)
