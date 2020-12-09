# views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django import forms
#from django.forms import RegisterForm
from .warehouse import WarehouseRegisterForm


#from account.forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            #form.save()
            return redirect("/warehouse/login")
    else:
        form = UserCreationForm()
    return render(request, 'warehouse/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/warehouse/warehouse')
    else:
        form = AuthenticationForm()
    return render(request, 'warehouse/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('warehouse/login')


def warehouse_register(response):
    if response.method == "POST":
	    form =WarehouseRegisterForm(response.POST)
	    if form.is_valid():
		    form.save()
	    return redirect("/main")
    else:
	    form =WarehouseRegisterForm()
	#return render(response, "/farmer.html", {"form":form})
    return render(response, 'warehouse/warehouse.html', {"form":form})

