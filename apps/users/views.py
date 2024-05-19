from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from apps.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import *

class RegisterView(View):

    def get(self, request):

        form = RegisterForm()
        return render(request, 'users/register.html', {"form":form})

    def post(self, request):

        form = RegisterForm(request.POST)

        if model_registeration(request, form):

            messages.success(request, "User succesfully registered")
            return redirect('users:login')
        
        messages.warning(request, "You`r registration is are not valid !")
        return render(request, "users/register.html", {"form":form})
    

class LoginView(View):
    def get(self, request):

        form = LoginForm()
        return render(request, 'users/login.html', {"form":form})

    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            if model_login(request, form):

                return redirect('gap:rooms')
            return redirect('users:login')
        
        return render(request, "users/login.html", {"form":form})


class LogoutView(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        return redirect('gap:rooms')
    
#--------------------------------------------

# class ProfileView(LoginRequiredMixin, View):

#     def get(self, request, id):
#         user = get_object_or_404(User, id=id)
#         form = ProfileForm(instance=user)
#         return render(request,"users/profile.html", {"form":form})
    
#     def post(self, request, id):
#         user = get_object_or_404(User, id=id)
#         form = ProfileForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User succsessfully updated")
#             return redirect('gap:rooms')
#         messages.warning(request, "your acount is not valid!")
#         return render(request,"index.html.html", {"form":form})