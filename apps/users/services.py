from django.db.models import Model
from django.forms import Form
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

def model_registeration(request, form:Form):
    if form.is_valid():
        form.save()
        return True
    return False

def model_login(request, form:Form):
    
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request=request, user=user)
        messages.success(request, F"{ username } you are logged ")
        return True
    
    messages.warning(request, "Invalid username or password !")
    return False