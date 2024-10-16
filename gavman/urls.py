from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    #path(render (request, 'authenticate/login.html'), {}),
    path('admin/', admin.site.urls, name="admin"),

    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('report', include('report.urls')),
    path('passport', include('passport.urls')),
    path("policy/", include("policy.urls")),
]+ staticfiles_urlpatterns()

