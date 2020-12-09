from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Crop

# class CropRegisterForm(UserCreationForm):
#     #email = forms.EmailField()
#     #model = Crop
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     product_type = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     product_name= forms.CharField(max_length=30, required=False, help_text='Optional.')
#     crop_stage = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     total_crop_quantity = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     daily_loading = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     required_temperature = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     required_relative_humidity = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     duration_of_storage = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     pick_up_location = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     drop_off_location = forms.CharField(max_length=30, required=False, help_text='Optional.')
#
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', "email", "product_type", "product_name","crop_stage", "total_crop_quantity", "daily_loading", "required_temperature", "required_relative_humidity", "duration_of_storage", "pick_up_location", "drop_off_location"]
class CropRegisterForm(forms.ModelForm):
    product_type = forms.CharField(max_length=30, required=False, help_text='Optional.')
    product_name= forms.CharField(max_length=30, required=False, help_text='Optional.')
    crop_stage = forms.CharField(max_length=30, required=False, help_text='Optional.')
    total_crop_quantity = forms.CharField(max_length=30, required=False, help_text='Optional.')
    daily_loading = forms.CharField(max_length=30, required=False, help_text='Optional.')
    required_temperature = forms.CharField(max_length=30, required=False, help_text='Optional.')
    required_relative_humidity = forms.CharField(max_length=30, required=False, help_text='Optional.')
    duration_of_storage = forms.CharField(max_length=30, required=False, help_text='Optional.')
    pick_up_location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    drop_off_location = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Crop
        fields = ["product_type", "product_name","crop_stage", "total_crop_quantity", "daily_loading", "required_temperature", "required_relative_humidity", "duration_of_storage", "pick_up_location", "drop_off_location"]
