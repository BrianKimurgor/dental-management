from django import forms
from dental_management.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['npi', 'name', 'email', 'phone_number', 'specialties', 'clinics']