from django.contrib import admin
from django.urls import path
from dental_management.views.clinic_views import clinic_list, clinic_detail, clinic_create, clinic_update, clinic_delete
from dental_management.views.doctor_views import doctor_list, doctor_detail, doctor_create, doctor_update, doctor_delete
from dental_management.views.specialty_views import specialty_list, specialty_detail, specialty_create, specialty_update, specialty_delete
from dental_management.views.patient_views import patient_list, patient_detail


urlpatterns = [
    #doctors
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor_detail'),
    path('doctors/create/', doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', doctor_delete, name='doctor_delete'),
    #specialties
    path('specialties/', specialty_list, name='specialty_list'),
    path('specialties/<int:pk>/', specialty_detail, name='specialty_detail'),
    path('specialties/create/', specialty_create, name='specialty_create'),
    path('specialties/<int:pk>/edit/', specialty_update, name='specialty_update'),
    path('specialties/<int:pk>/delete/', specialty_delete, name='specialty_delete'),

    
    path('patients/', patient_list, name='patient_list'),
    path('patients/<int:pk>/', patient_detail, name='patient_detail'),
    # clinics
    path('clinics/', clinic_list, name='clinic_list'),
    path('clinics/<int:pk>/', clinic_detail, name='clinic_detail'),
    path('clinics/create/', clinic_create, name='clinic_create'),  # This is the create URL pattern
    path('clinics/<int:pk>/edit/', clinic_update, name='clinic_update'),
    path('clinics/<int:pk>/delete/', clinic_delete, name='clinic_delete'),

]