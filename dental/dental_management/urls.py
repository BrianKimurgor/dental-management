from django.contrib import admin
from django.urls import path
from dental_management.views.clinic_views import clinic_list, clinic_detail, clinic_create, clinic_update, clinic_delete
from dental_management.views.doctor_views import doctor_list, doctor_detail
from dental_management.views.patient_views import patient_list, patient_detail


urlpatterns = [
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor_detail'),
    path('patients/', patient_list, name='patient_list'),
    path('patients/<int:pk>/', patient_detail, name='patient_detail'),
    # clinics
    path('clinics/', clinic_list, name='clinic_list'),
    path('clinics/<int:pk>/', clinic_detail, name='clinic_detail'),
    path('clinics/create/', clinic_create, name='clinic_create'),  # This is the create URL pattern
    path('clinics/<int:pk>/edit/', clinic_update, name='clinic_update'),
    path('clinics/<int:pk>/delete/', clinic_delete, name='clinic_delete'),

]