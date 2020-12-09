from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Warehouse

class WarehouseRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    warehouse_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    location= forms.CharField(max_length=30, required=False, help_text='Optional.')
    address = forms.CharField(max_length=30, required=False, help_text='Optional.')
    no_of_rooms = forms.CharField(max_length=30, required=False, help_text='Optional.')
    room_length = forms.CharField(max_length=30, required=False, help_text='Optional.')
    room_width = forms.CharField(max_length=30, required=False, help_text='Optional.')
    room_height = forms.CharField(max_length=30, required=False, help_text='Optional.')
    room_capacity = forms.CharField(max_length=30, required=False, help_text='Optional.')
    available_capacity = forms.CharField(max_length=30, required=False, help_text='Optional.')
    any_product_already_stored = forms.CharField(max_length=30, required=False, help_text='Optional.')
    refrigerant = forms.CharField(max_length=30, required=False, help_text='Optional.')
    refrigeration_capacity = forms.CharField(max_length=30, required=False, help_text='Optional.')
    room_temperature = forms.CharField(max_length=30, required=False, help_text='Optional.')
    relative_humidity = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Warehouse
        fields = ["warehouse_name", "location","address", "no_of_rooms", "room_length", "room_width", "room_height", "room_capacity", "available_capacity", "any_product_already_stored", "refrigerant","refrigeration_capacity","room_temperature", "relative_humidity"]