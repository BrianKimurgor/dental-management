from django.contrib import admin
from .models import Clinic, Doctor, Patient, Appointment, Visit, Specialty, Procedure

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'phone_number', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'npi', 'email', 'phone_number')
    filter_horizontal = ('specialties', 'clinics')  # For ManyToMany relationships

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'phone_number', 'ssn_last4')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'procedure', 'clinic', 'doctor', 'patient')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'clinic', 'doctor', 'patient')
    filter_horizontal = ('procedures',)

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name',)
