# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="passport.html"), name="passport"),

    path('check', views.checklist, name='check'),
    #path('s', views.submit_report, name='submit_report'),
   
 	] + staticfiles_urlpatterns()
