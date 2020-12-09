from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import crop_data

class CropDataForm(forms.ModelForm):
    crop_name = forms.CharField(max_length=200)
    quantity = forms.CharField(max_length=200)
    lat = forms.FloatField()
    lon = forms.FloatField()


class Meta:
        model = crop_data
        fields = ["crop_name","quantity", "lat", "lon"]