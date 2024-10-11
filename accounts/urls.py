from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.views.generic.base import TemplateView
from .views import register

urlpatterns = [

    path('home', TemplateView.as_view(template_name="home.html"), name="home"),
    path('signup/', register, name="signup"),
    path('', views.index, name='accounts'),
   #path('login', views.login_user, name="login"),
    #path("signup/", SignUpView.as_view(), name="signup"),

]+ staticfiles_urlpatterns()
