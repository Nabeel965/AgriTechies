from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('recommender/', views.crop_recommender, name='recommender'),
]