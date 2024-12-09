"""
URL configuration for dental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from dental_management.views.registration_view import register
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='dental_management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/',register, name='register'),
    path('admin/', admin.site.urls),
    path('dental_management/', include('dental_management.urls')),
    path('api/doctors/', include('dental_management.api.doctor.urls')),
    path('api/patients/', include ('dental_management.api.patients.urls')),
    path('api/clinics/', include('dental_management.api.clinics.urls')),
    path('api/appointments/', include('dental_management.api.appointments.urls')),
    path('api/visits/', include('dental_management.api.visits.urls')),
]
