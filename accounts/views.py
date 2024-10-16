from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .models import *
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'templates/registration/signup.html', {'form': form})
# Create your views here.

def index(request):
    return render(request, 'templates/authenticate/login.html')  
# Redirect to success page after successful submission

def registration(request):
    return render(request, 'templates/authenticate/registration/signup.html')  
# Redirect to success page after successful submission
