from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pandas as pd
import numpy as np
from .models import crop_data
from .recommender import CropDataForm

model = joblib.load('model.pkl')
xl_file = pd.ExcelFile('Features - Rev02.xlsx')
storage_df=xl_file.parse('Cold Storage Data')
crop_df=xl_file.parse('Crop Data')
# Create your views here.
def crop_recommender(response):
    if response.method == "POST":
        form = CropDataForm(response.POST)
        if form.is_valid():
            form=form.save(commit=False)
            return present_output(form)
    else:
        form = CropDataForm()
    return render(response, 'recommender/recommender.html', {"form":form})

def present_output(form):
    crop_name = form.crop_name
    quantity = form.quantity
    lat = form.lat
    lon = form.lon
    s = predict(crop_name, quantity, lat, lon)
    return HttpResponse(s)

def predict(Crop_Name,quantity,lat,lon):
  crop_temperature=crop_df['Required Temperature'][crop_df['Crop Name']==Crop_Name]
  crop_humidity=crop_df['Required Relative Humidity'][crop_df['Crop Name']==Crop_Name]
  lat=storage_df['lat']
  lon=storage_df['lon']
  quantity=storage_df['Avaiable Capacity']
  storage_temperature=storage_df['Room Temperature']
  storage_humidity=storage_df['Relative Humidity']
  temp_X=np.zeros((lat.shape[0],7))
  temp_X[:,0]=crop_temperature
  temp_X[:,1]=crop_humidity
  temp_X[:,2]=quantity
  temp_X[:,3]=storage_temperature
  temp_X[:,4]=storage_humidity
  temp_X[:,5]=lat
  temp_X[:,6]=lon

  return model.predict(temp_X)