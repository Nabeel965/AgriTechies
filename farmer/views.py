# views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django import forms
#from django.forms import RegisterForm
from .farmer import CropRegisterForm
from django.contrib.auth import login, logout


#Create your views here.
#from account.forms import RegisterForm
# Create your views here.
# def register(response):
# 	if response.method == "POST":
# 		form =RegisterForm(response.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("/home")
# 	else:
# 		form =RegisterForm()
# 	#return render(response, "/farmer.html", {"form":form})
# 	return render(response, 'farmer/register.html', {"form":form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            #form.save()
            return redirect("/farmer/login")
    else:
        form = UserCreationForm()
    return render(request, 'farmer/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/farmer/crop')
    else:
        form = AuthenticationForm()
    return render(request, 'farmer/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('farmer/login')


def crop_register(response):
    if response.method == "POST":
	    form =CropRegisterForm(response.POST)
	    if form.is_valid():
		    form.save()
	    return redirect("/main")
    else:
	    form =CropRegisterForm()
	#return render(response, "/farmer.html", {"form":form})
    return render(response, 'farmer/crop.html', {"form":form})

