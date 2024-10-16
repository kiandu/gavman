from django.shortcuts import render, redirect
#from .models import IncidentReport  # Replace with the actual name of your model
#from . forms import ReportForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
  return render(request, 'clearance.html')