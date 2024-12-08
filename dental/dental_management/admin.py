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
    # Update 'date' to 'date_time' to match the field in the Appointment model
    list_display = ('date_time', 'procedure', 'clinic', 'doctor', 'patient')
    list_filter = ('date_time', 'clinic', 'doctor')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    # Update 'date' to 'date_time' to match the field in the Visit model
    list_display = ('date_time', 'clinic', 'doctor', 'patient')
    list_filter = ('date_time', 'clinic', 'doctor')
    # Remove or replace filter_horizontal with a valid Many-to-Many field if applicable
    # For now, leaving it empty since Visit doesn't have a Many-to-Many field in the provided code
    filter_horizontal = []

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name',)
